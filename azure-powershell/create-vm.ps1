New-AzResourceGroup -Name "MyResourceGroup" -Location "EastUS"

New-AzVM `
  -ResourceGroupName "MyResourceGroup" `
  -Name "MyVM" `
  -Location "EastUS" `
  -VirtualNetworkName "MyVNet" `
  -SubnetName "MySubnet" `
  -SecurityGroupName "MyNSG" `
  -PublicIpAddressName "MyPublicIP" `
  -OpenPorts 80,3389
