# Approach 1

## Definitions

### Product

Can be:

- A software component identified by a software scanner (metaeffekt, SBOM generators)
- A CPE
- A PURL
- MS Product
- EOL Product
- ...

## Other criteria

- I feel like a "certainty" could be used here, that describes how certain the found match / relation is

## Method

Model the product data as a graph, where each node represents a product or a product relation.

### Product Nodes

Each product node identifies a single representation of a product.
This means that a node cannot refer to a 