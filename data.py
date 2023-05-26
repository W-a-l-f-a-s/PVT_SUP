WEBSITE_LIST = {"https://www.buzzfeed.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "quizzes" : 'partial link text;Quizzes',
                  "tvmovies" : 'partial link text;TV & Movies',
                  "shopping" : 'partial link text;Shopping',
                  "videos" : 'partial link text;Videos',
                  "news" : 'partial link text;News',
                  "food" : 'partial link text;Tasty',
                  "signin" : 'partial link text;Sign In',
                  "lolx3" : 'partial link text;lol Badge Feed',
                  "winner" : 'partial link text;win Badge Feed',
                  "trending" : 'partial link text;trending Badge Feed',
			"openmenu" : 'refresh_sens:css selector;[aria-label="open menu to see more links"]'
                 },
                  "sub-endpoints":
                  {
                      "openmenu" : {"aboutpg" : 'relies_prev:partial link text;About Us',
						"advertise" : 'relies_prev:partial link text;Advertise',
						"invest" : 'relies_prev:partial link text;Investor Relations',
						"getajob" : 'relies_prev:partial link text;Jobs',
						"merch" : 'relies_prev:partial link text;Merch',
						"newsletters" : 'relies_prev:partial link text;Newsletters',
						"leaderboard" : 'relies_prev:partial link text;Leaderboard',
                                   },
			    "aboutpg" : {"ceoboy" : 'class name;team_block-img'
                  }
                 }
                }

WEBSITE_LIST = {"https://ca.indeed.com":
                {"specifics":"ablock=true;",
                 "endpoints":
		    }
		   }

# INDEED DOES NOT ALLOW BOTS ANYWHERE ASIDE FROM THE HOMEPAGE





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
                      "aboutpg" : {"contact":'direct-link;contact_us.php',
                                   },
                      "upgradepg" : {"register":'direct-link;registration.php?pid=free',
                                     "registerbusiness":'direct-link;registration.php?pid=business_monthly_legacy',
                                     "registerpromonthly":'direct-link;registration.php?pid=premium_monthly',
                                     "registerproannually":'direct-link;registration.php?pid=premium_annual',
                                    },
                  }
                 }
                }

WEBSITE_LIST = {"https://open.spotify.com/":
		    {"specifics":"adblock=true;",
		     "endpoints":
		     {
			"signup" : 'css selector;button.Button-sc-1dqy6lx-0.jVdqg.sibxBMlr_oxWTfBrEz2G[data-encore-id="buttonTertiary"]',
			"login" : 'css selector;button[data-testid="login-button"]',
			"legal" : 'partial link text;Legal',
			"privacentre" : 'partial link text;Privacy Center',
			"cookies" : 'partial link text;Cookies',
			"accessibility" : 'partial link text;Accessibility',
			"about" : 'css selector;span[data-encore-id="type"].Type__TypeElement-sc-goli3j-0.gownZX',
			"jobs" : 'partial link text;Jobs',
			"news" : 'partial link text;For the Record',
		     },
			"sub-endpoints":
			{
				"search" : {"randgenre" : 'rand_ind:css selector;a.Em2LrSSfvrgXQoajs6cm'},
				"randgenre" : {"randmood" : 'partial link text;Show all'},
				"randmood" : {"randplaylist" : 'rand_ind:css selector;.image-wrapper a'},
				"legal" : {"copyright" : 'partial link text;Copyright Policy',
					     "privacy" : 'partial link text;Privacy Policy',
					     "guidelines" : 'partial link text;User Guidelines',
					     "premium" : 'partial link text;Premium Offer Terms',
					    },
				"privacentre" : {"protecc" : 'xpath;//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]' , 'partial link text;protecting your account'},
				"news" : {"randnews" : 'rand_ind:class name;box-border',
					    "fullnews" : 'css selector;a.button.hollow[href="/news"]'},
			 }
		      }
		     }

WEBSITE_LIST = {"https://www.flipkart.com/":
		    {"specifics":"adblock=true;",
		     "closesignup":'refresh_sens:xpath;//button[@class="_2KpZ6l _2doB4z"]',
		     "endpoints":
		     {
			"aboutus" : 'css selector;a._1arVWX[href="/about-us?otracker=undefined_footer_navlinks"]',
			"press" : 'css selector;a._1arVWX[href="/s/press?otracker=undefined_footer_navlinks"]',
			"corponews" : 'css selector;a._1arVWX[href="/corporate-information"]',
		     },
			"sub-endpoints":
			{
				"press" : {"randnews" : 'rand_ind~:css selector;article' , 'class name;read-more'},
				"randtrenditem" : {'rand_ind~:css selector;div._1GTrm1'},
			 }
		      }
		     }

WEBSITE_LIST = {"https://www.ladbible.com/":
		    {"specifics":"adblock=true;",
		     "endpoints":
		     {
			"randomfparticle" : 'rand_ind:css selector;article',
			"openmenu" : 'refresh_sens:css selector;button[data-cypress="menu-more"]',
		     },
			"sub-endpoints":
			{
				"submit" : 'direct-link;submit',
				"openmenu" : {"uokm8" : 'relies_prev:partial link text;UOKM8?',
						  "extinct" : 'relies_prev:direct-link;extinct',
						  "daily" : 'relies_prev:direct-link;daily-ladness',
						  "lfiles" : 'relies_prev:direct-link;lad-files',
						  "ftb" : 'relies_prev:direct-link;freetobe',
						  "citireef" : 'relies_prev:direct-link;citizenreef',
						 },
				"uokm8" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
				"extinct" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
				"daily" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
				"lfiles" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
				"ftb" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
				"citireef" : {"randarticle" : 'rand_ind:css selector;.image-wrapper a'},
			 }
		      }
		     }