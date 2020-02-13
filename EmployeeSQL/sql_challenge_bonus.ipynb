{
 "cells": [
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
    "engine = create_engine(f\"postgresql://{cfg.mysql['user']}:{cfg.mysql['passwd']}@{cfg.mysql['host']}:5432/sql_challenge\")\n",
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
      "text/plain": [
       "<Figure size 1224x720 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
    "fig=plt.figure(figsize=(17,10))\n",
    "df_salary.hist(column=\"salary\")\n",
    "plt.xlabel(\"Salary\",fontsize=15)\n",
    "plt.ylabel(\"Salary Value Frequency\",fontsize=15)\n",
    "plt.title(\"Salary Value Frequency vs. Salary (No Rounding)\")\n",
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
    "df_avgsalary[\"avg_salary\"] = df_avgsalary[\"avg_salary\"].astype(float).map('{:.2f}'.format)\n",
    "\n",
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
    "# Generate a bar plot showing the average salary by department\n",
    "plt.bar(df_avgsalary[\"dept_name\"], df_avgsalary[\"avg_salary\"])\n",
    "\n",
    "# Formatting\n",
    "plt.title(\"Average Salary By Department\")\n",
    "plt.xlabel(\"Department\")\n",
    "plt.ylabel(\"Average Salary\")\n",
    "# plt.ylim(0, 80000)\n",
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
