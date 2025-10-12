# Firebase Setup Guide

## Firebase Database Security Rules

Your Firebase Realtime Database currently has restricted access. To allow the application to work, you need to update the security rules:

### Step 1: Open Firebase Console
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Click on "Realtime Database" in the left menu

### Step 2: Update Security Rules
Click on the "Rules" tab and replace the existing rules with:

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

**Note:** These rules allow public read/write access. For production, you should implement proper authentication and use these rules instead:

```json
{
  "rules": {
    "products": {
      ".read": true,
      ".write": true
    },
    "customers": {
      ".read": true,
      ".write": true
    },
    "purchases": {
      "$userId": {
        ".read": true,
        ".write": true
      }
    }
  }
}
```

### Step 3: Publish Rules
Click "Publish" to apply the changes.

## ESP32/Raspberry Pi REST API Access

Firebase provides REST endpoints for devices that can't use the JavaScript SDK:

### Base URL Format
```
https://[PROJECT_ID].firebaseio.com/
```

### Read Data (GET)
```bash
curl 'https://[PROJECT_ID].firebaseio.com/products.json'
```

### Write Data (PUT)
```bash
curl -X PUT -d '{"id":"P001","name":"Product","quantity":10}' \
  'https://[PROJECT_ID].firebaseio.com/products/P001.json'
```

### Update Data (PATCH)
```bash
curl -X PATCH -d '{"quantity":5}' \
  'https://[PROJECT_ID].firebaseio.com/products/P001.json'
```

### Delete Data (DELETE)
```bash
curl -X DELETE \
  'https://[PROJECT_ID].firebaseio.com/products/P001.json'
```

### Query Parameters
- `?auth=[ID_TOKEN]` - For authenticated requests
- `?print=pretty` - Pretty-print JSON response
- `?shallow=true` - Get keys only

### Example for ESP32 (Arduino)
```cpp
#include <HTTPClient.h>
#include <WiFi.h>

String firebaseURL = "https://[PROJECT_ID].firebaseio.com";

void getProducts() {
  HTTPClient http;
  http.begin(firebaseURL + "/products.json");
  int httpCode = http.GET();
  
  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println(payload);
  }
  http.end();
}

void updateQuantity(String productId, int quantity) {
  HTTPClient http;
  http.begin(firebaseURL + "/products/" + productId + ".json");
  http.addHeader("Content-Type", "application/json");
  
  String data = "{\"quantity\":" + String(quantity) + "}";
  int httpCode = http.PATCH(data);
  
  http.end();
}
```

### Example for Raspberry Pi (Python)
```python
import requests

FIREBASE_URL = "https://[PROJECT_ID].firebaseio.com"

def get_products():
    response = requests.get(f"{FIREBASE_URL}/products.json")
    return response.json()

def update_quantity(product_id, quantity):
    data = {"quantity": quantity}
    response = requests.patch(
        f"{FIREBASE_URL}/products/{product_id}.json",
        json=data
    )
    return response.json()

def add_product(product):
    response = requests.put(
        f"{FIREBASE_URL}/products/{product['id']}.json",
        json=product
    )
    return response.json()
```

## Database Schema

```json
{
  "products": {
    "P001": {
      "id": "P001",
      "name": "Product Name",
      "quantity": 10,
      "expiryDate": "2025-12-31",
      "vendorPhone": "1234567890",
      "batchNumber": "BATCH001",
      "addedBy": "Vendor",
      "addedAt": "2025-10-12T00:00:00Z"
    }
  },
  "customers": {
    "customer1": "pass1",
    "customer2": "pass2"
  },
  "purchases": {
    "customer1": [
      {
        "productId": "P001",
        "productName": "Product Name",
        "date": "2025-10-12T00:00:00Z"
      }
    ]
  }
}
```

## Testing

After setting up the security rules, refresh the application and:

1. **Vendor Login** - Add a product
2. **Customer Login** - Login with customer1/pass1
3. **Purchase** - Buy a product
4. **Real-time Sync** - Open in multiple tabs and see changes sync automatically

## Troubleshooting

**Permission Denied Error:**
- Check that security rules are published
- Verify database URL is correct
- Make sure Firebase credentials are properly set

**Data Not Syncing:**
- Firebase uses real-time listeners (`onValue`) - no polling needed
- Check browser console for errors
- Verify internet connection

**ESP32/Pi Not Working:**
- Test REST endpoints with `curl` first
- Check URL format (must end with `.json`)
- Verify network connectivity
