WEBSITE_LIST = {"https://www.mediafire.com/":
                {"specifics":"ablock=true;",
                 "frontpage":'direct link;',
                 "endpoints":
                 { 
                  "upgradepg" : 'direct-link;upgrade',
                  "loginpg" : 'direct-link;login',
                  "aboutpg" : 'direct-link;about',
                  "softwarepg" : 'direct-link;software',
                  "adpg" : 'direct-link;advertising',
                  "creditspg" : 'direct-link;credits',
                  
                 },
                  "sub-endpoints":
                  {
                      "aboutpg" : {"contact":'relies_prev:direct-link;contact_us.php',
                                   },
                      "upgradepg":{"register":'relies_prev:direct-link;registration.php?pid=free',
                                   "registerbusiness":'relies_prev:direct-link;registration.php?pid=business_monthly_legacy',
                                   "registerpromonthly":'relies_prev:direct-link;registration.php?pid=premium_monthly',
                                   "registerproannually":'relies_prev:direct-link;registration.php?pid=premium_annual',
                                  },
                  }
                 }
                }