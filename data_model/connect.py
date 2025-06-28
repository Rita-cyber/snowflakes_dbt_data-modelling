{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import snowflake.connector\n",
    "\n",
    "conn = snowflake.connector.connect(\n",
    "    user=os.getenv(\"SNOWFLAKE_USER\"),\n",
    "    password=os.getenv(\"SNOWFLAKE_PASSWORD\"),\n",
    "    account=os.getenv(\"SNOWFLAKE_ACCOUNT\"),\n",
    "    warehouse=os.getenv(\"SNOWFLAKE_WAREHOUSE\"),\n",
    "    database=os.getenv(\"SNOWFLAKE_DATABASE\"),\n",
    "    schema=os.getenv(\"SNOWFLAKE_SCHEMA\")\n",
    ")\n",
    "\n",
    "cursor = conn.cursor()\n",
    "cursor.execute(\"SELECT CURRENT_VERSION()\")\n",
    "print(cursor.fetchone())\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
