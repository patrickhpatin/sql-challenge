{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# SQL Challenge\n",
    "\n",
    "## Assumptions for the TA grading my assignment:\n",
    "\n",
    "### 1. You are using a postgres database\n",
    "### 2. Your database uses port 5432 or change it in the \"databaseconfig.py\" file\n",
    "### 3. You will need to edit the \"databaseconfig.py\" file with your connection information to test the bonus Jupyter Notebook\n",
    "### 4. The PGAdmin SQL Tool has a few major limitations.  For instance, there's no way to declare a variable for csv_path.  I tried several different ways to no avail.  In addition, there is no way to use relative pathing to the csv files either.  I tried several ways to do this as well to no avail.  Due to these limitations, you will need to change the path to the CSV files, for every csv file we import, to test the inport functionality.  I apologize but it's not my fault.\n",
    "### 5. There's some abiguity to a few of the questions in the SQL portion of this project such as: 3, 4, 6 and 7. I have interpreted these as asking to find all CURRENT employees. For example, #6 - List all emloyees in the Sales department (i.e. NOT all employees who have EVER BEEN in the sales department).  If an employee has a to_date in the past, that employee is NO LONGER in the sales department and therefore should NOT be in the list.\n",
    "\n",
    "### I know it's a bit early but...\n",
    "\n",
    "\n",
    "<img src=\"AprilFools.png\" alt=\"April Fools!\" style=\"border: none;\" /><br>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import psycopg2\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import databaseconfig as cfg\n",
    "import pandas.io.sql as sqlio\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from pandas import DataFrame\n",
    "from sqlalchemy import create_engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "      <th>from_date</th>\n",
       "      <th>to_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>14024</td>\n",
       "      <td>24024</td>\n",
       "      <td>40000</td>\n",
       "      <td>1993-03-14</td>\n",
       "      <td>1994-03-14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>40329</td>\n",
       "      <td>50329</td>\n",
       "      <td>40000</td>\n",
       "      <td>1994-12-17</td>\n",
       "      <td>1995-12-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>16406</td>\n",
       "      <td>26406</td>\n",
       "      <td>40000</td>\n",
       "      <td>1993-04-12</td>\n",
       "      <td>1994-04-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>16397</td>\n",
       "      <td>26397</td>\n",
       "      <td>40000</td>\n",
       "      <td>1995-01-12</td>\n",
       "      <td>1996-01-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>12743</td>\n",
       "      <td>22743</td>\n",
       "      <td>40000</td>\n",
       "      <td>1999-10-30</td>\n",
       "      <td>2000-10-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300019</th>\n",
       "      <td>27558</td>\n",
       "      <td>37558</td>\n",
       "      <td>125469</td>\n",
       "      <td>1989-02-23</td>\n",
       "      <td>1990-02-23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300020</th>\n",
       "      <td>258327</td>\n",
       "      <td>458302</td>\n",
       "      <td>126703</td>\n",
       "      <td>1998-10-05</td>\n",
       "      <td>1999-10-05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300021</th>\n",
       "      <td>244781</td>\n",
       "      <td>444756</td>\n",
       "      <td>127041</td>\n",
       "      <td>1999-06-14</td>\n",
       "      <td>2000-06-13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300022</th>\n",
       "      <td>34188</td>\n",
       "      <td>44188</td>\n",
       "      <td>127238</td>\n",
       "      <td>1991-03-16</td>\n",
       "      <td>1992-03-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300023</th>\n",
       "      <td>105025</td>\n",
       "      <td>205000</td>\n",
       "      <td>129492</td>\n",
       "      <td>1991-10-12</td>\n",
       "      <td>1992-10-11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>300024 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            id  emp_no  salary   from_date     to_date\n",
       "0        14024   24024   40000  1993-03-14  1994-03-14\n",
       "1        40329   50329   40000  1994-12-17  1995-12-17\n",
       "2        16406   26406   40000  1993-04-12  1994-04-12\n",
       "3        16397   26397   40000  1995-01-12  1996-01-12\n",
       "4        12743   22743   40000  1999-10-30  2000-10-29\n",
       "...        ...     ...     ...         ...         ...\n",
       "300019   27558   37558  125469  1989-02-23  1990-02-23\n",
       "300020  258327  458302  126703  1998-10-05  1999-10-05\n",
       "300021  244781  444756  127041  1999-06-14  2000-06-13\n",
       "300022   34188   44188  127238  1991-03-16  1992-03-15\n",
       "300023  105025  205000  129492  1991-10-12  1992-10-11\n",
       "\n",
       "[300024 rows x 5 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Database connection string\n",
    "engine = create_engine(f\"postgresql://{cfg.mysql['user']}:{cfg.mysql['passwd']}@{cfg.mysql['host']}:{cfg.mysql['port']}/{cfg.mysql['db']}\")\n",
    "\n",
    "# Create a database connection\n",
    "conn = engine.connect()\n",
    "\n",
    "# Pull salary information from our database\n",
    "sql = \"SELECT * FROM salaries ORDER BY salary ASC;\"\n",
    "df_salary = pd.read_sql(sql, conn)\n",
    "\n",
    "# Pull average salaries by title\n",
    "sql = \"SELECT titles.title, AVG(salaries.Salary) AS Avg_Salary FROM salaries \"\n",
    "sql = sql + \"INNER JOIN titles ON titles.emp_no = salaries.emp_no GROUP BY titles.title ORDER BY AVG(salaries.Salary) ASC;\"\n",
    "df_avgsalarybytitle = pd.read_sql(sql, conn)\n",
    "\n",
    "# Where's Waldo?\n",
    "sql = \"SELECT emp_no, first_name, last_name FROM employees WHERE emp_no = 499942;\"\n",
    "df_myself = pd.read_sql(sql, conn)\n",
    "\n",
    "# Make sure we close our connection to the database\n",
    "conn.close()\n",
    "\n",
    "df_salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('$40,000', '$129,492')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Min & Max Salaries\n",
    "min_salary = '${:0,.0f}'.format(df_salary[\"salary\"].min())\n",
    "max_salary = '${:0,.0f}'.format(df_salary[\"salary\"].max())\n",
    "\n",
    "# Show our min and max salaries\n",
    "min_salary, max_salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1224x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Histogram\n",
    "fig=plt.figure(figsize=(17,10))\n",
    "plt.hist(df_salary[\"salary\"])\n",
    "plt.xlabel(\"Employee Salary ($ USD)\", fontsize=15)\n",
    "plt.ylabel(\"Salary Value Frequency\",fontsize=15)\n",
    "plt.ylim(0, 160000)\n",
    "plt.title(\"Salary Value Frequency vs. Salary (No Rounding)\", fontsize=18)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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3LKqbp/kkUlO7u6Lu/uSJCcnOXDcdvPu/mB3d5JjZ44FAAAAO43tNoe/qvZOct8kH0py2+7+SjJcFEhym7HanknOm9lt41i2qfKNS5QDAADATmW7BP6q+oEkb03yvO6+dFNVlyjrLShfqg2HVdX6qlp/0UUXba7JAAAAcJ2yzQN/Vd0gQ9h/U3f/21h8wTgcP+PzhWP5xiR3nNl9ryTnb6Z8ryXKr6W7j+zudd29bo899ti6DwUAAAA7mG29Sn8lOSrJp7v7L2Y2nZBkYaX9Q5IcP1N+8Lha//5JvjEO+T8pyQFVtdu4WN8BSU4at32zqvYfz3XwzLEAAABgp7HLNj7fg5L8cpIzq+rjY9nvJnlVkuOq6tAkX07yuHHbiUkenWRDku8keWqSdPfFVfWKJB8Z6728uy8eXz8zydFJdk3yzvEBAAAAO5VtGvi7+31Zep59kjxsifqd5FnLHOsNSd6wRPn6JPfaimYCAADAdd52W6UfAAAAWDsCPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAADABAn8AAAAMEECPwAAAEyQwA8AAAATJPADAP9/e3cer10973/89a5bg+ZBUVJRKaQkUdI8EjKFjihDp5AjZDhklnOO6ZRwDk6UoQznKEkSFZVQhAZSkerXHCrN5fP747u2rm53qe6999rX2q/n47Ef+7rWWvvan/te+1rX+nyH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\n",
      "text/plain": [
       "<Figure size 1224x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Generate a bar plot showing the average salary by title\n",
    "fig=plt.figure(figsize=(17,10))\n",
    "plt.bar(df_avgsalarybytitle[\"title\"], df_avgsalarybytitle[\"avg_salary\"])\n",
    "\n",
    "# Formatting\n",
    "plt.ylim(0, 70000)\n",
    "plt.title(\"Average Salary By Position Title\", fontsize=18)\n",
    "plt.xlabel(\"Position Title\", fontsize=15)\n",
    "plt.ylabel(\"Average Salary\", fontsize=15)\n",
    "plt.xticks(rotation=70)\n",
    "\n",
    "# Show the chart\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>499942</td>\n",
       "      <td>April</td>\n",
       "      <td>Foolsday</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   emp_no first_name last_name\n",
       "0  499942      April  Foolsday"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find myself:  Employee_ID = 499942\n",
    "df_myself"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
