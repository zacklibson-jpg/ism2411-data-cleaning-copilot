What Copilot Generated

With Copilot, I made the first iterations of two functions, `load_raw_sales` and `standardize_colnames`. I prompted Copilot with `Load raw sales data from CSV` and `Standardize column names`. Copilot had simple implementations for those functions, and I took those and modified them a bit from their original iterations.

What I Modified

More complex logic was added for data quality improvements, such as field normalization, quote removal from text fields, and consistency of column aliases, along with additional functions for dealing with empty placeholders and for zero-value row deletion. Those improvements addressed assignment requirements for a messy dataset.

What I Learned

I learned that data cleaning is a stepwise process, and also learned that column name standardization, validation and cleaning of data entries, and missing values handling are also parts of the process. The type of work Copilot provides is excellent for basic structure of the code, but for the actual work, input is still needed. I had to write the logic to remove category name quotes and to drop zero quantity rows, since Copilot did not include those.

