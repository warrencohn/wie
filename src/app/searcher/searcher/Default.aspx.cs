using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Data;
using Newtonsoft.Json;

namespace searcher
{
    public partial class _Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
            }

        }
        protected void btnsSubmit_Click(object sender, EventArgs e)
        {
            if (ddlsType.SelectedIndex == 0)
            {
                string[] diachi;
                string chitiet = txtsName.Text;
                string whereclause = "";
                if (IsNumber(chitiet[0].ToString()))
                {
                    diachi = txtsName.Text.Trim().Split(new char[] { ' ' }, 2);
                    if (diachi.Length == 2)
                        whereclause = "WHERE SoNha LIKE '%" + diachi[0] + "%' AND DuongKhongDau LIKE N'%" + diachi[1] + "%'";
                }
                else
                {
                    whereclause = "WHERE DuongKhongDau LIKE N'%" + txtsName.Text + "%'";
                }
                if (whereclause != "")
                {
                    string sql = "SELECT * FROM tbl_CongTy WHERE DiaChiId IN (SELECT  id FROM tbl_DiaChi " + whereclause + ")";
                    DataTable list = Database.GetData(sql);
                    dlResult.DataSource = list;
                    dlResult.DataBind();
                }
                else
                {
                    dlResult.DataSource = null;
                    dlResult.DataBind();
                    //Response.Redirect(Request.Url.ToString());
                }
            }
            else { }
        }

        [System.Web.Services.WebMethodAttribute(), System.Web.Script.Services.ScriptMethodAttribute()]
        public static string[] GetCompletionList(string prefixText, int count, string contextKey)
        {
            //string sql = "Select duong from DiaChi Where duong like '" + prefixText + "' + '%'";
            string sql = "SELECT DISTINCT DuongKhongDau FROM tbl_DiaChi WHERE Duong LIKE N'%" + prefixText + "%' OR DuongKhongDau LIKE N'%" + prefixText + "%'";
            SqlDataAdapter da = new SqlDataAdapter(sql, Database.GetConnection());
            DataTable dt = new DataTable();
            da.Fill(dt);
            string[] items = new string[dt.Rows.Count];
            int i = 0;
            foreach (DataRow dr in dt.Rows)
            {
                items.SetValue(dr[0].ToString(), i);
                i++;
            }
            return items;
        }
        static bool IsNumber(string value)
        {
            // Return true if this is a number.
            int number1;
            return int.TryParse(value, out number1);
        }
    }
}
