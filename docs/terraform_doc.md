brew install terraform-docs

https://terraform-docs.io/reference/markdown-document/

``` bash
terraform-docs markdown document [PATH] [flags]
terraform-docs markdown document . >> ../docs/example.tf.md

```
https://www.terraform.io/docs/cli/commands/graph.html
``` bash
$ terraform graph | dot -Tsvg > graph.svg
```

Compute 

=== "Azure"

    ``` c
    terraform {
    required_providers {
        azurerm = {
        source  = "hashicorp/azurerm"
        version = "=2.46.0"
        }
    }
    }
    ```

=== "AWS"

    ``` c
    terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 3.0"
        }
    }
    }
    ```

=== "GCP"

    ``` terraform
    provider "google" {
    project     = "my-project-id"
    region      = "us-central1"
    }
    ```

!!! Note
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
   nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
   massa, nec semper lorem quam in massa.

???+ note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

!!! info inline end
    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.

???+ Tip
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa. Tip

++ctrl+alt+del++

:smile: 