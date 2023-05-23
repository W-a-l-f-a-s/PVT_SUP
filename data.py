WEBSITE_LIST = {"https://www.flipkart.com/":
		    {"specifics":"adblock=true;",
		     "closesignup":'xpath;//button[@class="_2KpZ6l _2doB4z"]',
		     "endpoints":
		     {
			"aboutus" : 'css selector;a._1arVWX[href="/about-us?otracker=undefined_footer_navlinks"]',
			"news" : 'css selector;a._1arVWX[href="/s/press?otracker=undefined_footer_navlinks"]',
			"corponews" : 'css selector;a._1arVWX[href="/corporate-information"]',
		     },
			"sub-endpoints":
			{
				"news" : {"randnews" : 'rand_ind~:css selector;article' , 'class name;read-more',
					    },
				"randtrenditem" : {'rand_ind~:css selector;div._1GTrm1',
							 },
			 }
		      }
		     }