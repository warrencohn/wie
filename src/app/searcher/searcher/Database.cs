using System;
using System.Data;
using System.Configuration;
using System.Web;
using System.Web.Configuration;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;
using System.Data.SqlClient;

namespace searcher
{
    public static class Database
    {
        public static String conStr = "Data Source=(local);Initial Catalog=BDDemo;Integrated Security=True";
        public static SqlConnection GetConnection()
        {
            return new SqlConnection(conStr);
        }
        public static DataTable GetData(String sql, params Object[] parameters)
        {
            return Database.Fill(new DataTable(), sql, parameters);
        
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
        public static int ExecuteNonQuery(String sql, params Object[] parameters)
        {
            SqlCommand command = Database.CreateCommand(sql, parameters);

            command.Connection.Open();
            int rows = command.ExecuteNonQuery();
            command.Connection.Close();

            return rows;
        }
    }
}