# QR Code Features Documentation

## Overview
The Multi-User Product Manager now includes comprehensive QR code generation and scanning capabilities for both vendors and customers, enabling quick product management and purchases.

## Vendor QR Code Features

### 1. Automatic QR Code Generation
**When it happens:**
- Automatically generates when a vendor adds a new product
- Automatically generates when a vendor updates an existing product

**What's included in the QR code:**
- Product ID
- Product Name
- Quantity
- Expiry Date
- Vendor Phone
- Batch Number

**How it works:**
1. Vendor fills out the product form
2. Clicks "Add Product" or "Update Product"
3. Product is saved to Firebase
4. QR code is automatically generated with all product details
5. Application automatically switches to the "QR Codes" tab
6. QR code is displayed along with product information

### 2. QR Code Display
**Location:** Vendor Dashboard → 📷 QR Codes tab

The generated QR code is displayed with:
- High-resolution 256x256 pixel QR code
- Complete product information below the code
- Download button to save as PNG file

### 3. Download QR Code
**Feature:** Vendors can download the generated QR code as a PNG image file

**How to use:**
1. After adding/updating a product, the QR code appears in the QR Codes tab
2. Click the "📥 Download QR Code" button
3. The QR code is saved as `product-[ID]-qr.png`

**Use cases:**
- Print QR codes for product labels
- Share QR codes with customers
- Create product catalogs
- Physical inventory management

### 4. Vendor QR Scanner
**Location:** Vendor Dashboard → 📷 QR Codes tab

**Purpose:** Scan product QR codes to quickly auto-fill the product form for updates

**How to use:**
1. Go to Vendor Dashboard → QR Codes tab
2. Click "Start Scanner"
3. Allow camera access if prompted
4. Point camera at a product QR code
5. Scanner automatically reads the QR code
6. Product details are auto-filled in the form
7. Application switches to Products tab
8. Form is ready for editing with "Update Product" button

**Benefits:**
- Quick product updates without manual typing
- Reduces data entry errors
- Perfect for mobile devices
- Fast inventory management

## Customer QR Code Features

### Customer QR Scanner
**Location:** Customer Dashboard → 📷 QR Scanner tab

**Purpose:** Scan product QR codes to quickly purchase items

**How to use:**
1. Login as a customer
2. Go to QR Scanner tab
3. Click "Start Scanner"
4. Scan a product QR code
5. Product details appear with "Purchase Now" button
6. Click to complete the purchase

**Benefits:**
- Fast checkout process
- Works with printed product labels
- Mobile-friendly shopping experience
- No need to search through product lists

## QR Code Format

### Data Structure
QR codes contain JSON data with the following structure:

```json
{
  "id": "P001",
  "name": "Product Name",
  "quantity": 50,
  "expiryDate": "2025-12-31",
  "vendorPhone": "1234567890",
  "batchNumber": "BATCH001"
}
```

### Technical Details
- **Format:** JSON string
- **Size:** 256x256 pixels
- **Error Correction:** High (Level H)
- **Color:** Black on white background
- **Encoding:** UTF-8

## Use Cases

### Retail Store
1. Vendor adds products with QR codes
2. Print QR codes and attach to physical products
3. Customers scan QR codes to see details and purchase
4. Inventory automatically updates

### Warehouse Management
1. Generate QR codes for all inventory items
2. Use QR scanner to quickly update quantities
3. Track expiry dates and batch numbers
4. Fast stocktaking with mobile devices

### Mobile Shopping
1. Customers use smartphones to scan products
2. Instant product information display
3. One-click purchase process
4. Real-time inventory updates

### Product Catalog
1. Generate QR codes for all products
2. Create printed catalogs with QR codes
3. Customers scan to get latest pricing and availability
4. Digital catalog with physical touchpoints

## Browser Compatibility

### Camera Access Required
- Chrome 53+ (desktop and mobile)
- Firefox 63+ (desktop and mobile)
- Safari 11+ (iOS and macOS)
- Edge 79+

### QR Code Generation
- All modern browsers with Canvas support
- Works offline once libraries are loaded

## Troubleshooting

### Camera Not Working
**Issue:** Scanner won't start or camera access denied

**Solutions:**
1. Grant camera permission in browser settings
2. Use HTTPS connection (required for camera access)
3. Check if another app is using the camera
4. Try different browser

### QR Code Won't Scan
**Issue:** Scanner can't read the QR code

**Solutions:**
1. Ensure good lighting conditions
2. Hold camera steady and at proper distance
3. Make sure QR code is not damaged or blurry
4. Check if QR code is from this application

### Download Not Working
**Issue:** QR code download button doesn't work

**Solutions:**
1. Allow downloads in browser settings
2. Check popup blocker settings
3. Ensure sufficient storage space
4. Try different browser

### Scanner Auto-Fills Wrong Data
**Issue:** Scanned data doesn't match the QR code

**Solutions:**
1. Ensure QR code is from this application
2. Check for damaged or partial QR codes
3. Rescan the code
4. Generate new QR code if needed

## Integration with ESP32/Raspberry Pi

### QR Code Data Format
ESP32 and Raspberry Pi devices can generate compatible QR codes using standard JSON format:

```python
# Python example for Raspberry Pi
import json
import qrcode

product_data = {
    "id": "P001",
    "name": "Product Name",
    "quantity": 50,
    "expiryDate": "2025-12-31",
    "vendorPhone": "1234567890",
    "batchNumber": "BATCH001"
}

qr_data = json.dumps(product_data)
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("product_qr.png")
```

```cpp
// Arduino/ESP32 example
#include <ArduinoJson.h>
#include <qrcode.h>

void generateQRCode(String id, String name, int quantity) {
  StaticJsonDocument<200> doc;
  doc["id"] = id;
  doc["name"] = name;
  doc["quantity"] = quantity;
  doc["expiryDate"] = "2025-12-31";
  doc["vendorPhone"] = "1234567890";
  doc["batchNumber"] = "BATCH001";
  
  String qrData;
  serializeJson(doc, qrData);
  
  // Generate QR code with qrData
  // Display on OLED or print to thermal printer
}
```

## Security Considerations

### Data Privacy
- QR codes contain product information only
- No sensitive customer data in QR codes
- Customer purchase data stored securely in Firebase

### Access Control
- Only vendors can generate QR codes
- Only logged-in customers can make purchases
- Firebase security rules control data access

### Best Practices
1. Don't share QR codes of expired products
2. Regenerate QR codes after significant updates
3. Verify scanned data before processing
4. Use HTTPS for all connections

## Future Enhancements

Potential improvements for QR features:
- Batch QR code generation for multiple products
- QR code customization (colors, logos)
- QR code analytics (scan tracking)
- Encrypted QR codes for sensitive data
- Dynamic QR codes that update automatically
- NFC tag integration
- Barcode support (in addition to QR codes)
