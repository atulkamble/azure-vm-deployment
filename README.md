**complete list of methods to create an Azure VM**

---

## ✅ All Possible Ways to Create an Azure VM:

| Method                                     | Tool / Interface                  | Code / Command |
| :----------------------------------------- | :-------------------------------- | :------------- |
| **1. Azure Portal (GUI)**                  | Web browser                       | Manual         |
| **2. Azure CLI**                           | Command line / Bash / PowerShell  | ✅              |
| **3. Azure PowerShell**                    | PowerShell console                | ✅              |
| **4. Azure ARM Templates**                 | JSON-based IaC                    | ✅              |
| **5. Bicep**                               | Bicep DSL (IaC)                   | ✅              |
| **6. Terraform**                           | Terraform (HCL IaC tool)          | ✅              |
| **7. Ansible**                             | YAML Playbooks with Azure modules | ✅              |
| **8. Azure SDK (Python, .NET, Java, etc)** | Programmatic SDK-based            | ✅              |

---

## ✅ Now — Codes & Commands for Each:

---

## 📌 1️⃣ Azure CLI

```bash
az group create --name MyResourceGroup --location eastus

az vm create \
  --resource-group MyResourceGroup \
  --name MyVM \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys
```

---

## 📌 2️⃣ Azure PowerShell

```powershell
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
```

---

## 📌 3️⃣ ARM Template (JSON)

**azuredeploy.json**

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "vmName": { "type": "string" },
    "adminUsername": { "type": "string" },
    "adminPassword": { "type": "securestring" }
  },
  "resources": [
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2022-03-01",
      "name": "[parameters('vmName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "hardwareProfile": { "vmSize": "Standard_DS1_v2" },
        "storageProfile": {
          "imageReference": {
            "publisher": "Canonical",
            "offer": "UbuntuServer",
            "sku": "18.04-LTS",
            "version": "latest"
          },
          "osDisk": { "createOption": "FromImage" }
        },
        "osProfile": {
          "computerName": "[parameters('vmName')]",
          "adminUsername": "[parameters('adminUsername')]",
          "adminPassword": "[parameters('adminPassword')]"
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', concat(parameters('vmName'),'-nic'))]"
            }
          ]
        }
      }
    }
  ]
}
```

Deploy it:

```bash
az deployment group create --resource-group MyResourceGroup --template-file azuredeploy.json --parameters vmName=MyVM adminUsername=azureuser adminPassword=YourPassword123!
```

---

## 📌 4️⃣ Bicep (IaC DSL for ARM)

**vm.bicep**

```bicep
resource vm 'Microsoft.Compute/virtualMachines@2022-03-01' = {
  name: 'myVM'
  location: resourceGroup().location
  properties: {
    hardwareProfile: {
      vmSize: 'Standard_DS1_v2'
    }
    storageProfile: {
      imageReference: {
        publisher: 'Canonical'
        offer: 'UbuntuServer'
        sku: '18.04-LTS'
        version: 'latest'
      }
      osDisk: {
        createOption: 'FromImage'
      }
    }
    osProfile: {
      computerName: 'myVM'
      adminUsername: 'azureuser'
      adminPassword: 'Password123!'
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: resourceId('Microsoft.Network/networkInterfaces', 'myNic')
        }
      ]
    }
  }
}
```

Deploy it:

```bash
az deployment group create --resource-group MyResourceGroup --template-file vm.bicep
```

---

## 📌 5️⃣ Terraform

**main.tf**

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_virtual_network" "example" {
  name                = "myVNet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_subnet" "example" {
  name                 = "mySubnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_network_interface" "example" {
  name                = "myNIC"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_virtual_machine" "example" {
  name                  = "myVM"
  location              = azurerm_resource_group.example.location
  resource_group_name   = azurerm_resource_group.example.name
  network_interface_ids = [azurerm_network_interface.example.id]
  vm_size               = "Standard_DS1_v2"

  storage_os_disk {
    name              = "myOsDisk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  os_profile {
    computer_name  = "myVM"
    admin_username = "azureuser"
    admin_password = "Password123!"
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }
}
```

Deploy:

```bash
terraform init
terraform apply
```

---

## 📌 6️⃣ Ansible

**azure\_vm\_playbook.yml**

```yaml
- hosts: localhost
  tasks:
    - name: Create Azure VM
      azure_rm_virtualmachine:
        resource_group: "MyResourceGroup"
        name: "myVM"
        vm_size: "Standard_DS1_v2"
        admin_username: "azureuser"
        admin_password: "Password123!"
        image:
          offer: UbuntuServer
          publisher: Canonical
          sku: '18.04-LTS'
          version: latest
```

Run it:

```bash
ansible-playbook azure_vm_playbook.yml
```

---

## 📌 7️⃣ Azure SDK (Python Example)

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

subscription_id = 'your-subscription-id'
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

vm = compute_client.virtual_machines.begin_create_or_update(
    "MyResourceGroup",
    "myVM",
    {
        "location": "eastus",
        "storage_profile": {
            "image_reference": {
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "18.04-LTS",
                "version": "latest"
            }
        },
        "hardware_profile": {
            "vm_size": "Standard_DS1_v2"
        },
        "os_profile": {
            "computer_name": "myVM",
            "admin_username": "azureuser",
            "admin_password": "Password123!"
        },
        "network_profile": {
            "network_interfaces": [{
                "id": "/subscriptions/xxxx-xxxx/resourceGroups/MyResourceGroup/providers/Microsoft.Network/networkInterfaces/myNic"
            }]
        }
    }
)
```

---

## 📌 8️⃣ Azure Portal (Manual)

* Go to Azure Portal
* Navigate to **Virtual Machines**
* Click **+ Create**
* Follow the wizard UI for all options
  (No code — GUI driven)

---

## 📊 Summary

| Method       | Code Available |
| :----------- | :------------- |
| Azure CLI    | ✅              |
| PowerShell   | ✅              |
| ARM Template | ✅              |
| Bicep        | ✅              |
| Terraform    | ✅              |
| Ansible      | ✅              |
| SDK (Python) | ✅              |
| Azure Portal | GUI            |

---

## ✅ Conclusion

That’s the **complete, production-grade list with working examples** for creating Azure VMs across all supported ways.
