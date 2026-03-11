import sqlite3
import os
import datetime

# Define the path to the database file
DB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DB_PATH = os.path.join(DB_DIR, 'leads_database.sqlite')

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def setup_database():
    """Creates the necessary tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create leads table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            url TEXT,
            business_type TEXT,
            location TEXT,
            status TEXT DEFAULT 'New',
            deal_value REAL DEFAULT 0.0,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create indexes to speed up lookups and prevent duplicates
    # A lead is duplicate if it has the same name AND (phone OR url)
    # However, for simplicity, let's just make phone unique if it exists
    cursor.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS idx_leads_phone ON leads(phone) WHERE phone IS NOT NULL AND phone != ''
    ''')
    
    conn.commit()
    conn.close()

def add_lead(name, phone=None, url=None, business_type=None, location=None):
    """Adds a new lead to the database. Returns True if successful, False if it's a duplicate."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Check if lead already exists by phone (if provided)
        if phone:
            cursor.execute("SELECT id FROM leads WHERE phone = ?", (phone,))
            if cursor.fetchone():
                return False # Duplicate by phone
                
        # Check if lead already exists by name and url (if both provided)
        if name and url:
            cursor.execute("SELECT id FROM leads WHERE name = ? AND url = ?", (name, url))
            if cursor.fetchone():
                return False # Duplicate by name and url
                
        cursor.execute('''
            INSERT INTO leads (name, phone, url, business_type, location)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, phone, url, business_type, location))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # This will catch the unique index constraint on phone
        return False
    finally:
        conn.close()

def get_all_leads():
    """Returns all leads from the database."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row # To access columns by name
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads ORDER BY created_at DESC")
    leads = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return leads

def update_lead_status(lead_id, new_status, notes=None, deal_value=None):
    """Updates the status and other details of a lead."""
    conn = get_connection()
    cursor = conn.cursor()
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    update_query = "UPDATE leads SET status = ?, updated_at = ?"
    params = [new_status, now]
    
    if notes is not None:
        update_query += ", notes = ?"
        params.append(notes)
        
    if deal_value is not None:
        update_query += ", deal_value = ?"
        params.append(deal_value)
        
    update_query += " WHERE id = ?"
    params.append(lead_id)
    
    cursor.execute(update_query, tuple(params))
    conn.commit()
    conn.close()

def get_analytics_data():
    """Returns aggregated data for the dashboard."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Total leads by status
    cursor.execute("SELECT status, COUNT(*) as count FROM leads GROUP BY status")
    status_counts = {row['status']: row['count'] for row in cursor.fetchall()}
    
    # Total deal value
    cursor.execute("SELECT SUM(deal_value) as total_value FROM leads WHERE status IN ('Interested', 'Closed', 'Pitched')")
    row = cursor.fetchone()
    total_deal_value = row['total_value'] if row['total_value'] else 0.0
    
    # Leads by location
    cursor.execute("SELECT location, COUNT(*) as count FROM leads WHERE location IS NOT NULL GROUP BY location")
    location_counts = {row['location']: row['count'] for row in cursor.fetchall()}
    
    conn.close()
    
    return {
        "status_counts": status_counts,
        "total_deal_value": total_deal_value,
        "location_counts": location_counts
    }

# Run setup when the module is imported
setup_database()
