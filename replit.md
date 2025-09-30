# Multi-User Product Manager

## Overview
A real-time shared product management system built as a static HTML application. The application allows vendors to manage product inventory and customers to purchase products, with real-time synchronization using JSONBin.io as a backend.

## Project Type
- **Frontend**: Static HTML/CSS/JavaScript single-page application
- **Backend**: JSONBin.io (external API service)
- **Server**: Python HTTP server for serving static files

## Recent Changes (September 30, 2025)
- Imported project from GitHub
- Configured Python HTTP server to serve static files from `docs/` directory
- Set up workflow to run on port 5000
- Configured deployment settings for autoscale deployment
- Added cache-control headers to prevent browser caching issues

## Project Structure
```
.
├── docs/
│   └── index.html          # Main application file (HTML/CSS/JS)
├── server.py              # Python HTTP server
├── README.md             # Project documentation
└── replit.md             # This file
```

## How It Works
1. Users select their role (Vendor or Customer)
2. Configure JSONBin.io credentials to enable multi-user functionality
3. Vendors can add, edit, and delete products with expiry tracking
4. Customers can view and purchase available products
5. All changes sync in real-time across all users via JSONBin.io

## Configuration
- The application requires JSONBin.io credentials (Bin ID and Secret Key)
- Users configure these credentials through the web interface
- Credentials are stored in browser localStorage

## Running Locally
The server runs on port 5000 and serves files from the `docs/` directory with cache-control headers to prevent stale content.

## Deployment
Configured for autoscale deployment, suitable for this stateless web application.
