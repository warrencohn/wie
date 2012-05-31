using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.SqlClient;
using System.Data;

namespace searcher
{
    public static class Database
    {
        public static String conStr = "Data Source=HUNGVJNH\\SQLEXPRESS;Initial Catalog=BDSG;Integrated Security=True";
        public static SqlConnection GetConnection()
        {
            return new SqlConnection(conStr);
        }
        public static DataTable GetData(String sql, params Object[] parameters)
        {
            return Database.Fill(new DataTable(), sql, parameters);
        }
        public static DataTable Fill(DataTable table, String sql, params Object[] parameters)
        {
            SqlCommand command = Database.CreateCommand(sql, parameters);
            new SqlDataAdapter(command).Fill(table);
            command.Connection.Close();

            return table;
        }
        private static SqlCommand CreateCommand(String sql, params Object[] parameters)
        {
            SqlCommand command = new SqlCommand(sql, Database.GetConnection());
            for (int i = 0; i < parameters.Length; i += 2)
            {
                command.Parameters.AddWithValue(parameters[i].ToString(), parameters[i + 1]);
            }
            return command;
        }
    }
}