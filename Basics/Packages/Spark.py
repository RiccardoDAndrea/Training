{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pyspark'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[11], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdatetime\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m datetime, date\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mpyspark\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01msql\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Row\n\u001b[1;32m      4\u001b[0m df \u001b[38;5;241m=\u001b[39m spark\u001b[38;5;241m.\u001b[39mcreateDataFrame([\n\u001b[1;32m      5\u001b[0m     Row(a\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m1\u001b[39m, b\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2.\u001b[39m, c\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstring1\u001b[39m\u001b[38;5;124m'\u001b[39m, d\u001b[38;5;241m=\u001b[39mdate(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m1\u001b[39m), e\u001b[38;5;241m=\u001b[39mdatetime(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m12\u001b[39m, \u001b[38;5;241m0\u001b[39m)),\n\u001b[1;32m      6\u001b[0m     Row(a\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2\u001b[39m, b\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3.\u001b[39m, c\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstring2\u001b[39m\u001b[38;5;124m'\u001b[39m, d\u001b[38;5;241m=\u001b[39mdate(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m1\u001b[39m), e\u001b[38;5;241m=\u001b[39mdatetime(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m, \u001b[38;5;241m12\u001b[39m, \u001b[38;5;241m0\u001b[39m)),\n\u001b[1;32m      7\u001b[0m     Row(a\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m4\u001b[39m, b\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5.\u001b[39m, c\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstring3\u001b[39m\u001b[38;5;124m'\u001b[39m, d\u001b[38;5;241m=\u001b[39mdate(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m3\u001b[39m, \u001b[38;5;241m1\u001b[39m), e\u001b[38;5;241m=\u001b[39mdatetime(\u001b[38;5;241m2000\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m3\u001b[39m, \u001b[38;5;241m12\u001b[39m, \u001b[38;5;241m0\u001b[39m))\n\u001b[1;32m      8\u001b[0m ])\n\u001b[1;32m      9\u001b[0m df\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pyspark'"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date\n",
    "import pandas as pd\n",
    "from pyspark.sql import Row\n",
    "df = spark.createDataFrame([\n",
    "    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),\n",
    "    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),\n",
    "    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))\n",
    "])\n",
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "mnist",
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
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
