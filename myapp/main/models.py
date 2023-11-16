from django.db import models


class Data(models.Model):
    Job = models.TextField()
    JV = models.TextField()
    Batch = models.TextField()
    Ref = models.TextField()
    Acct = models.TextField()
    # Map the column name to the correct field
    Acct_Desc = models.TextField(db_column='Acct Desc')
    Dept = models.TextField()
    # Map the column name to the correct field
    Dept_Desc = models.TextField(db_column='Dept Desc')
    Tran_Date = models.DateField(primary_key=True, db_column='Tran Date')
    Desc = models.TextField()
    # Map the column name to the correct field
    Invoice_Nbr = models.TextField(db_column='Invoice Nbr')
    Amt = models.TextField()
    # Map the column name to the correct field
    Acct_Per = models.TextField(db_column='Acct Per')
    Comment = models.TextField()
    # Map the column name to the correct field
    Due_Date = models.TextField(db_column='Due Date')
    # Map the column name to the correct field
    Chk_Date = models.TextField(db_column='Chk Date')
    Sequence = models.TextField()
    # Map the column name to the correct field
    Batch_Close_Date = models.TextField(db_column='Batch Close Date')
    # Map the column name to the correct field
    Vend_Cust_Nbr = models.TextField(db_column='Vend/Cust Nbr')

    class Meta:
        managed = False  # Specify that Django should not manage this table
        db_table = 'data'  # Specify the table name in the database
