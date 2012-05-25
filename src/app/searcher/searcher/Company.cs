using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace searcher
{
    public class Company
    {
        public Company()
        {
            //
            // TODO: Add constructor logic here
            //
        }
        [JsonProperty]
        public string Name { get; set; }
        [JsonProperty]
        public string Address { get; set; }
        [JsonProperty]
        public string Phone { get; set; }
        [JsonProperty]
        public string Fax { get; set; }
        [JsonProperty]
        public string Email { get; set; }
        [JsonProperty]
        public string Website { get; set; }
        [JsonProperty]
        public string X { get; set; }
        [JsonProperty]
        public string Y { get; set; }
    }
}