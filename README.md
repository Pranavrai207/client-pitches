# Client Pitches: Premium Website Generator

Welcome to our automated client website generator! This tool creates beautiful, custom-designed websites for local businesses like salons, cafes, and gyms. Every site we generate automatically includes mobile-friendly layouts, beautiful images, and unique custom designs.

## 🌐 Live Portfolio

All our sample websites are deployed live on GitHub Pages. Click any of the links below to see the sites in action:

### 💇 Salons & Beauty
- **Hairgenix Salon** - [View Site](https://pranavrai207.github.io/client-pitches/clients/hairgenix_salon/)
- **Images Unisex Saloon** - [View Site](https://pranavrai207.github.io/client-pitches/clients/images_unisex_saloon/)
- **In Style Hair Salon** - [View Site](https://pranavrai207.github.io/client-pitches/clients/in_style_hair_salon/)
- **J Salon** - [View Site](https://pranavrai207.github.io/client-pitches/clients/j_salon/)
- **Posh by Charms** - [View Site](https://pranavrai207.github.io/client-pitches/clients/posh_premium/)
- **Martina Wu** - [View Site](https://pranavrai207.github.io/client-pitches/clients/martina_wu/)

### 🍽️ Restaurants & Cafes
- **ShellBeacon Cafe, Bar & Kitchen** - [View Site](https://pranavrai207.github.io/client-pitches/clients/shellbeacon_cafe/)
- **Mr. K Ramyun Cafe** - [View Site](https://pranavrai207.github.io/client-pitches/clients/mr_k_ramyun_cafe/)
- **Impresario** - [View Site](https://pranavrai207.github.io/client-pitches/clients/impresario/)
- **The Golden Spoon** - [View Site](https://pranavrai207.github.io/client-pitches/clients/the-golden-spoon/)
- **Reflections Cafe** - [View Site](https://pranavrai207.github.io/client-pitches/clients/reflections_cafe/)
- **FoodCourt House Takeaway** - [View Site](https://pranavrai207.github.io/client-pitches/clients/foodcourt_house_takeway/)
- **7Heaven Foods** - [View Site](https://pranavrai207.github.io/client-pitches/clients/7heaven_foods/)

### 💪 Fitness & Wellness
- **Power Zone Gym** - [View Site](https://pranavrai207.github.io/client-pitches/clients/power_zone_gym/)
- **Real Steel Gym** - [View Site](https://pranavrai207.github.io/client-pitches/clients/real-steel-gym/)
- **Neon Genesis Fitness** - [View Site](https://pranavrai207.github.io/client-pitches/clients/neon-genesis-fitness/)
- **Yoga For World** - [View Site](https://pranavrai207.github.io/client-pitches/clients/yoga-for-world/)

### 🎭 Other Experiences
- **Dance with Shubham** - [View Site](https://pranavrai207.github.io/client-pitches/clients/dance-with-shubham/)

---

## 🚀 How to Use

Follow these simple steps to run the application on your computer:

**1. Install the Requirements**
Make sure you have Python installed. Open your command prompt or terminal and type:
```bash
pip install -r requirements.txt
playwright install chromium
```

**2. Generate a New Website**
Want to build a new site for a new client? Just run this command with the client's name:
```bash
python main.py pitch --client "Your Client Name"
```

**3. Put the Site Online**
Once the site is built locally, you can publish it to the live portfolio with one easy command:
```bash
python main.py deploy --client "your_client_folder_name"
```

That's it! Your new website is now live and ready to show to your client.
