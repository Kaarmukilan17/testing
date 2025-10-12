# Multi-User Product Manager

## Overview
A real-time shared product management system built with Firebase Realtime Database. The application allows vendors to manage product inventory with QR code generation and customers to purchase products with QR scanning capabilities, featuring real-time synchronization and modern UI with dark mode.

## Project Type
- **Frontend**: Static HTML/CSS/JavaScript single-page application
- **Backend**: Firebase Realtime Database (real-time sync)
- **Server**: Python HTTP server with Firebase config injection
- **QR Libraries**: QRCode.js (generation) and html5-qrcode (scanning)

## Recent Changes (October 12, 2025)
### Major Updates
- ✅ Migrated from JSONBin.io to Firebase Realtime Database
- ✅ Added real-time sync using Firebase onValue listeners (removed polling)
- ✅ Implemented modern UI with dark/light theme toggle
- ✅ Fixed all reported bugs (vendor edit, purchase quantity, expiry alerts)
- ✅ Added comprehensive QR code features for vendors and customers

### New Features
1. **Vendor QR Code Generation**
   - Automatic QR code generation when adding/updating products
   - QR codes contain all product details (ID, name, quantity, expiry, phone, batch)
   - Downloadable as PNG files
   
2. **Vendor QR Scanner**
   - Scan product QR codes to auto-fill form for quick updates
   - Camera-based scanning with html5-qrcode library
   
3. **Customer QR Scanner**
   - Scan product QR codes for quick purchases
   - Mobile-friendly shopping experience
   
4. **Vendor Customer Management**
   - Create customer accounts with username/password
   - Prevent duplicate usernames
   
5. **Purchase History Export**
   - Customers can export their purchase history as CSV
   
6. **Analytics Dashboard**
   - Vendor can view total products, customers, low stock, and expiring items
   
7. **Dark Mode**
   - Toggle between light and dark themes
   - Preference saved in localStorage

## Project Structure
```
.
├── docs/
│   └── index.html              # Main application (HTML/CSS/JS)
├── server.py                   # Python HTTP server with Firebase config injection
├── FIREBASE_SETUP.md          # Firebase setup and ESP32/Pi integration guide
├── QR_CODE_FEATURES.md        # Complete QR code features documentation
├── README.md                  # Project documentation
└── replit.md                  # This file
```

## How It Works

### Vendor Workflow
1. Login as Vendor
2. Add/update products → QR codes automatically generated
3. View products with expiry alerts
4. Scan QR codes to quickly update product info
5. Download QR codes for printing/sharing
6. Manage customer accounts
7. View analytics dashboard

### Customer Workflow
1. Login with username/password
2. Browse available products
3. Scan QR codes or click to purchase
4. View purchase history
5. Get expiry alerts for purchased products only
6. Export purchase history as CSV

### Real-Time Sync
- Firebase onValue listeners for automatic updates
- No manual refresh needed
- Changes appear instantly across all devices/tabs
- Proper data persistence with merge operations

## Firebase Configuration
- Environment variables injected via server.py
- Required secrets: FIREBASE_API_KEY, FIREBASE_AUTH_DOMAIN, FIREBASE_DATABASE_URL, etc.
- Security rules must be configured in Firebase Console (see FIREBASE_SETUP.md)

## Database Schema
```json
{
  "products": {
    "productId": {
      "id": "string",
      "name": "string", 
      "quantity": "number",
      "expiryDate": "date",
      "vendorPhone": "string",
      "batchNumber": "string",
      "addedBy": "string",
      "addedAt": "timestamp"
    }
  },
  "customers": {
    "username": "password"
  },
  "purchases": {
    "customerId": [
      {
        "productId": "string",
        "productName": "string",
        "date": "timestamp"
      }
    ]
  }
}
```

## QR Code Features
- **Generation**: Automatic QR code creation on product add/update
- **Scanning**: Camera-based QR scanning for vendors and customers
- **Download**: Export QR codes as PNG files
- **Format**: JSON data with all product details
- **Size**: 256x256 pixels with high error correction

## Running Locally
The server runs on port 5000 and serves files from the `docs/` directory with:
- Cache-control headers to prevent stale content
- Firebase environment variable injection
- Static file serving for HTML/CSS/JS

## Deployment
Configured for autoscale deployment, suitable for this stateless web application.

## ESP32/Raspberry Pi Integration
See FIREBASE_SETUP.md for:
- Firebase REST API endpoints
- Python and Arduino/ESP32 code examples
- QR code generation for IoT devices
- Database access without JavaScript SDK

## Bug Fixes Implemented
1. ✅ Vendor edit persistence - products now save correctly without page reload
2. ✅ Customer purchase quantity - quantities properly decrement in Firebase
3. ✅ Product visibility - all vendor products appear in customer dashboard
4. ✅ Customer expiry alerts - only show alerts for products customer purchased

## Technologies Used
- Firebase Realtime Database (v10.7.1)
- QRCode.js (v1.0.0) - QR code generation
- html5-qrcode (v2.3.8) - QR code scanning
- Python 3.11 HTTP server
- Vanilla JavaScript (ES6+)
- CSS3 with CSS Variables for theming
