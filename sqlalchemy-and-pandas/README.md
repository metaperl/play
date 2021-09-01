# Example of Change in session.query() in SQLAlchemy 

When calling `session.query()` with specific column names, version 1.3.20 of 
SQLAlchemy returns column data that pandas can use
to create a dataframe with labelled columns. Version 1.4.23 of SA does
not.

In other words, with version 1.3.20 of SA, you can simply pass one argument
to [the constructor of a pandas Dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
and that argument alone creates a dataframe with column names that are the
same as the attribute names of the ORM class used to represent the table.

In contrast, with version 1.4.23 of SA, the very same code, leads to
construction of a Pandas dataframe that has numeric column names - for some
reason, the results of `session.query()` are not as descriptive.

# Installation Instructions

    shell> pip install -r requirements.txt

This will install the latest pandas and SQLAlchemy 1.3.20

# Now examine the generated dataframe with SQLAlchemy 1.3.20

    shell> python a.py

Notice that the columns of the Pandas dataframe have names equivalent
to the names of the database columns described in the SA schema:

```
  name   fullname
0   ed   Ed Jones
1  ted  TEd Jones
2  red  rEd Jones
```

I.e: the columns are named `name` and `fullname`.

# Now install SQLAlchemy 1.4.23

    shell> pip install sqlalchemy==1.4.23

## Now notice that the dataframe has numeric column names instead of names similar to the columns from SA

```
     0          1
0   ed   Ed Jones
1  ted  TEd Jones
2  red  rEd Jones
```

I.e: the columns are labelled `0` and `1` instead of `name` and `fullname`.

# Question

How can we get back the 1.3.20 behavior of `session.query()` in 1.4 and 2.0
SQLAlchemy?

