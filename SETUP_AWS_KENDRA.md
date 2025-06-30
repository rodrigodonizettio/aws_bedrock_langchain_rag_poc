# AWS KENDRA

Here are the steps to create the Amazon Kendra that'll be used in the cloud provider to store the data content for AWS Bedrock Knowledge Base (KB).

The configurations were done using **AWS Management Console**.

## Index Setup

- Amazon Kendra > Create an Index
    - Fill the form
        - Choose Index name
        - IAM role
            - Create a new role
            - Choose Role name
        - Click on Next
        - Choose an edition
            - Developer edition
        - Click on Next
    - Click on Create

### S3 Data Source Setup

- Amazon Kendra > Indexes > Choose your previous created index > Add data source
    - Search for the Amazon S3 connector > Add connector
        - Fill the form
            - Choose Data source name
            - Default language of source documents
                - English (en)
            - Click on Next
            - IAM role
                - Create a new role
                - Choose Role name
            - Click on Next
            - Sync scope
                - Enter the data source location
                    - Paste the S3 Bucket Name
                - Additional configuration
                    - Include patterns
                        - Type: Prefix
                        - Prefix: place the rest of the URI prefix where you stored your [Employee-Handbook.pdf](aws_bedrock/Employee-Handbook.pdf) file
            - Sync mode
                - Choose New, modified, or deleted content sync (on the first sync it'll perform a full sync)
            - Sync run schedule
                - Choose Run on demand
            - Click on Next
            - S3 field mapping guide
            - Click on Next
        - Click on Add data source

### Web Crawler Data Source Setup

- Amazon Kendra > Indexes > Choose your previous created index > Add data source
    - Search for the Web Crawler v2.0 connector > Add connector
        - Fill the form
            - Choose Data source name
            - Default language of source documents
                - English (en)
            - Click on Next
            - Source
                - Choose Source URLs
                - Source URLs
                    - https://kinetecoinc.com
                - IAM role
                - Create a new role
                - Choose Role name
            - Click on Next
            - Sync scope
                - Sync domains only
            - Sync mode
                - Full sync
            - Sync run schedule
                - Choose Run on demand
            - Click on Next
            - Field mapping guide
            - Click on Next
        - Click on Add data source

#### Data Source Sync

- Amazon Kendra > Data management > Data sources > Choose your previous created data source > Sync now