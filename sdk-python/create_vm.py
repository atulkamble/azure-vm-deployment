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
