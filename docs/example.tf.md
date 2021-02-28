## Requirements

The following requirements are needed by this module:

- azurerm (=2.46.0)

## Providers

The following providers are used by this module:

- azurerm (=2.46.0)

## Modules

No Modules.

## Resources

The following resources are used by this module:

- [azurerm_resource_group](https://registry.terraform.io/providers/hashicorp/azurerm/2.46.0/docs/resources/resource_group)
- [azurerm_virtual_network](https://registry.terraform.io/providers/hashicorp/azurerm/2.46.0/docs/resources/virtual_network)

## Required Inputs

No required input.

## Optional Inputs

No optional input.

## Outputs

No output.
Usage:

Example of 'foo\_bar' module in `foo_bar.tf`.

- list item 1
- list item 2

Even inline **formatting** in _here_ is possible.  
and some [link](https://domain.com/)

* list item 3
* list item 4

```hcl
module "foo_bar" {
  source = "github.com/foo/bar"

  id   = "1234567890"
  name = "baz"

  zones = ["us-east-1", "us-west-1"]

  tags = {
    Name         = "baz"
    Created-By   = "first.last@email.com"
    Date-Created = "20180101"
  }
}
```

Here is some trailing text after code block,  
followed by another line of text.

| Name | Description     |
|------|-----------------|
| Foo  | Foo description |
| Bar  | Bar description |

## Requirements

The following requirements are needed by this module:

- terraform (>= 0.12)

- terraform (>= 0.12)

- aws (>= 2.15.0)

- aws (>= 2.15.0)

- azurerm (=2.46.0)

- random (>= 2.2.0)

- random (>= 2.2.0)

## Providers

The following providers are used by this module:

- aws (>= 2.15.0 >= 2.15.0)

- aws.ident (>= 2.15.0 >= 2.15.0)

- azurerm (=2.46.0)

- null

- tls

## Modules

The following Modules are called:

### bar

Source: baz

Version: 4.5.6

### baz

Source: baz

Version: 4.5.6

### foo

Source: bar

Version: 1.2.3

## Resources

The following resources are used by this module:

- [aws_caller_identity](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity)
- [azurerm_resource_group](https://registry.terraform.io/providers/hashicorp/azurerm/2.46.0/docs/resources/resource_group)
- [azurerm_virtual_network](https://registry.terraform.io/providers/hashicorp/azurerm/2.46.0/docs/resources/virtual_network)
- [null_resource](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource)
- [tls_private_key](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key)

## Required Inputs

No required input.

## Optional Inputs

No optional input.

## Outputs

No output.
