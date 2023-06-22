from cvplibrary import Form

# Set local variables from Forms

vlan_id = Form.getFieldById('vlan_id').getValue()
svi = Form.getFieldById('svi').getValue()
svi_mask = Form.getFieldById('svi_mask').getValue()

# Generate VLAN DB entry

print("vlan %s") % vlan_id
  
# Generate SVI

print("interface vlan %s") % vlan_id
print("   ip address %s/%s") % (svi, svi_mask)