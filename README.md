# testing


# Product Management System — Firebase & QR Integration

This repository is a product management web app supporting multi-user vendor/customer actions, real-time updates with Firebase, and QR code features for inventory management and purchases.

## Features
- **Real-time product sync**—uses Firebase Realtime Database
- **Vendor dashboard:** Add/edit products, manage inventory, generate QR codes for product details
- **Customer features:** Scan QR to purchase, view purchase history, analytics
- **QR code integration:** Auto-generate QR for each product; scan QR to auto-fill or update product info
- **CSV export, analytics dashboard, REST API** for IoT device integration (e.g., ESP32/ Raspberry Pi)
- **Modern UI:** Responsive design, light/dark mode, tab interaction

---

## Getting Started

### 1. Clone or Download

Clone this repo, or download as ZIP and extract.

### 2. Firebase Setup

- Go to [Firebase Console](https://console.firebase.google.com/)
- Create/select your project
- Enable Realtime Database (Test Mode for now)
- Copy your project’s config (apiKey, authDomain, etc.)
- Update `.env` or equivalent config in your hosting setup as per `FIREBASE_SETUP.md`

**Set database rules:**  
Use the rules from `FIREBASE_SETUP.md` for initial public testing.

### 3. Run/Host

- **On Replit:** Just click “Run” to preview.
- **On Local/Static Host:** Open `index.html` in your browser.
- **On GitHub Pages:** Push the latest code and visit `https://<your-username>.github.io/<repo-name>/`

> ⚠️ Note: `server.py` is only for simulating a backend server when testing on Replit. It is NOT needed for static deployment on GitHub Pages.
(server.py is not in the final version but can be found in the previous commits)
---

## Using the App

#### Vendors
- Open the app and **login as a vendor** (if authentication, else select vendor dashboard)
- **Add a product:** Fill out Product ID, Name, Quantity, Expiry, Vendor Phone, Batch Number
- **After adding, a QR code is shown.** Download/print it if needed for physical tagging.
- **To update product:** Go to the "QR Codes" tab, start scanner, scan the QR, auto-fill/edit and save.

#### Customers
- Go to Customer dashboard (if implemented)
- **Scan QR code** on product to view/buy, automatically updates database
- Download CSV of purchases, view analytics, etc.

#### IoT Integration
- See `QR_CODE_FEATURES.md` and `FIREBASE_SETUP.md` for REST API, ESP32/Pi examples.

---

## File Overview

- `index.html` — Main app frontend  
- `FIREBASE_SETUP.md` — Firebase credentials & database setup  
- `QR_CODE_FEATURES.md` — QR code usage, format, and troubleshooting  
- `server.py` — Replit testing only (not needed for static/GitHub hosting)  
- `.replit` / `replit.md` — Replit config/instructions 

---

## FAQ

- **Can I remove `server.py` for GitHub Pages hosting?**  
  Yes, unless you plan to use Replit or any Python server. GitHub Pages only needs static files.

- **What files are required for GitHub Pages?**  
  - `index.html`, asset folders (like `/docs`), JavaScript/CSS, your markdown docs.

- **How do I test all features?**  
  - Add/update products as vendor  
  - Scan QR codes to add/purchase/update  
  - View dashboards, export CSV, try IoT API if needed

---

## Support

See included markdown files or open an issue if stuck.
