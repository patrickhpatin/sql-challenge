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
    "### 2. Your database uses port 5432\n",
    "### 3. You will need to edit the \"databaseconfig.py\" file with your connection information\n",
    "\n",
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
    "engine = create_engine(f\"postgresql://{cfg.mysql['user']}:{cfg.mysql['passwd']}@{cfg.mysql['host']}:5432/{cfg.mysql['db']}\")\n",
    "\n",
    "# Create a database connection\n",
    "conn = engine.connect()\n",
    "\n",
    "# Pull salary information from our database\n",
    "sql = \"SELECT * FROM salaries ORDER BY salary ASC;\"\n",
    "df_salary = pd.read_sql(sql, conn)\n",
    "\n",
    "# Pull average salaries by department\n",
    "sql = \"SELECT d.dept_name AS Dept_Name, AVG(sal.Salary) AS Avg_Salary FROM salaries AS sal \"\n",
    "sql = sql + \"INNER JOIN dept_emp AS de ON de.emp_no = sal.emp_no INNER JOIN departments AS d ON d.dept_no = de.dept_no \"\n",
    "sql = sql + \"GROUP BY d.dept_name ORDER BY d.dept_name ASC;\"\n",
    "df_avgsalary = pd.read_sql(sql, conn)\n",
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
       "<Figure size 432x288 with 1 Axes>"
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
    "df_salary.hist(column=\"salary\")\n",
    "plt.xlabel(\"Salary\", fontsize=15)\n",
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
       "      <th>dept_name</th>\n",
       "      <th>avg_salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Customer Service</td>\n",
       "      <td>47998.67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Development</td>\n",
       "      <td>48697.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Finance</td>\n",
       "      <td>59533.52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Human Resources</td>\n",
       "      <td>44678.65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Marketing</td>\n",
       "      <td>61095.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Production</td>\n",
       "      <td>48760.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Quality Management</td>\n",
       "      <td>46456.01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Research</td>\n",
       "      <td>48850.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Sales</td>\n",
       "      <td>69832.13</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            dept_name avg_salary\n",
       "0    Customer Service   47998.67\n",
       "1         Development   48697.33\n",
       "2             Finance   59533.52\n",
       "3     Human Resources   44678.65\n",
       "4           Marketing   61095.90\n",
       "5          Production   48760.45\n",
       "6  Quality Management   46456.01\n",
       "7            Research   48850.19\n",
       "8               Sales   69832.13"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Format average salaries and round to 2 decimal places\n",
    "df_avgsalary[\"avg_salary\"] = df_avgsalary[\"avg_salary\"].astype(float).map('{:.2f}'.format)\n",
    "\n",
    "# Show our data\n",
    "df_avgsalary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
    "# Generate a bar plot showing the average salary by department\n",
    "fig=plt.figure(figsize=(17,10))\n",
    "plt.bar(df_avgsalary[\"dept_name\"], df_avgsalary[\"avg_salary\"])\n",
    "\n",
    "# Formatting\n",
    "plt.title(\"Average Salary By Department\", fontsize=18)\n",
    "plt.xlabel(\"Department\", fontsize=15)\n",
    "plt.ylabel(\"Average Salary\", fontsize=15)\n",
    "plt.xticks(rotation=70)\n",
    "\n",
    "# Show the chart\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
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
     "execution_count": 7,
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
