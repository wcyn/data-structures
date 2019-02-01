## SQL Performance and More

Learning about:
- Query performance
- Joins
- SQL injection

### Setting up sample data

_(Data samples are from the interviewcake site)_

It contains four cakes, a million customers, and a million orders:

1. In your terminal, download our script and start up MySQL:

```
$ curl -O https://static.interviewcake.com/bakery_schema_and_data.sql && mysql.server start && mysql -u root
```

2. Run the downloaded script to set up the BAKERY database and insert data:

```
> source bakery_schema_and_data.sql;
```
  
 
