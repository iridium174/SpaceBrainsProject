﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BusinessLogic.Services.Base
{
    public interface IAuthenticationService
    {
        bool CheckUser(string login, string password);
        bool IsAdmin(string login);
    }
}
