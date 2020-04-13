from bs4 import BeautifulSoup

soup = BeautifulSoup('''
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <thead>
                  <tr>
                    <th rowspan="2" align="left" valign="top" class="TAL" width="215">Company Name</th>
                    <th colspan="2" width="260">Price at</th>
                    <th rowspan="2" valign="top" width="140">Change*</th>
                    <th rowspan="2" valign="top" width="140">%Gain*</th>
                    <th rowspan="2" valign="top" width="140">Current price</th>
                  </tr>
                  <tr>
                    <th align="center" style="text-align:center;">15:00</th>
                    <th align="center" style="text-align:center;">16:00</th>
                  </tr>
                </thead>
                <tbody>
				                  <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/telecommunicationsservice/nettlinx/NS05" style="text-decoration:none;color:#333333">Nettlinx</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE027D01019','BSE','511658');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nettlinx AGM on Sep 25, 2019||Announcement date: Aug 09, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">24.00</td>
                    <td align="right" width="130">27.45</td>
                    <td align="right" width="140">3.45</td>
                    <td align="right" width="140">14.38</td>
                    <td align="right" width="140">27.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/jtlinfra/JTL01" style="text-decoration:none;color:#333333">JTL Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE391J01016','BSE','534600');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>JTL Infra - Outcome of AGM</span></a></li><li><a href="javascript:void(0)"><span>JTL Infra's AGM on September 28, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/jtlinfra/notices/JTL01" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>JTL Infra has hit 52wk low of Rs 70.10 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">112.00</td>
                    <td align="right" width="130">121.85</td>
                    <td align="right" width="140">9.85</td>
                    <td align="right" width="140">8.79</td>
                    <td align="right" width="140">121.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/breweriesdistilleries/jagatjitindustries/JI01" style="text-decoration:none;color:#333333">Jagatjit Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE574A01016','BSE','507155');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Jagatjit Ind closes above 50-Day Moving Average of 26.89 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">24.70</td>
                    <td align="right" width="130">26.75</td>
                    <td align="right" width="140">2.05</td>
                    <td align="right" width="140">8.30</td>
                    <td align="right" width="140">26.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electricals/finelinecircuits/FC" style="text-decoration:none;color:#333333">Fine-line Circ</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE087E01011','BSE','517264');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Fine-line Circ closes above 30-Day Moving Average of 26.74 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">26.45</td>
                    <td align="right" width="130">28.60</td>
                    <td align="right" width="140">2.15</td>
                    <td align="right" width="140">8.13</td>
                    <td align="right" width="140">28.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/saveraindustries/SH" style="text-decoration:none;color:#333333">Savera Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE104E01014','BSE','512634');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Savera Ind's board meeting held on Aug 09, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/saveraindustries/notices/SH" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Savera Ind closes above 50-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">42.50</td>
                    <td align="right" width="130">45.80</td>
                    <td align="right" width="140">3.30</td>
                    <td align="right" width="140">7.76</td>
                    <td align="right" width="140">45.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/foodprocessing/milkfood/M04" style="text-decoration:none;color:#333333">Milkfood</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE588G01013','BSE','507621');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Milkfood EGM on Feb 07, 2020||Announcement date: Jan 10, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">477.00</td>
                    <td align="right" width="130">513.00</td>
                    <td align="right" width="140">36.00</td>
                    <td align="right" width="140">7.55</td>
                    <td align="right" width="140">513.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/premierpolyfilm/PP19" style="text-decoration:none;color:#333333">Premier Polyfil</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE309M01012','BSE','514354');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Premier Polyfil closes above 50-Day Moving Average of 22.58 today.</span></li><li><span>Premier Polyfil closes below 50-Day Moving Average of 22.41 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">21.30</td>
                    <td align="right" width="130">22.80</td>
                    <td align="right" width="140">1.50</td>
                    <td align="right" width="140">7.04</td>
                    <td align="right" width="140">22.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/auto23wheelers/majesticauto/MA01" style="text-decoration:none;color:#333333">Majestic Auto</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE201B01022','BSE','500267');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Majestic Auto AGM on Sep 28, 2019||Announcement date: Aug 30, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">100.15</td>
                    <td align="right" width="130">107.00</td>
                    <td align="right" width="140">6.85</td>
                    <td align="right" width="140">6.84</td>
                    <td align="right" width="140">107.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/asianhotelswest/AHW" style="text-decoration:none;color:#333333">Asian Hotel (W)</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE915K01010','BSE','533221');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Asian Hotel (W) closes below 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">292.05</td>
                    <td align="right" width="130">311.95</td>
                    <td align="right" width="140">19.90</td>
                    <td align="right" width="140">6.81</td>
                    <td align="right" width="140">311.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/ramaphosphates/RP07" style="text-decoration:none;color:#333333">Rama Phosphates</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE809A01024','BSE','524037');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rama Phosphates closes above 30-Day Moving Average of 42.29 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">41.20</td>
                    <td align="right" width="130">44.00</td>
                    <td align="right" width="140">2.80</td>
                    <td align="right" width="140">6.80</td>
                    <td align="right" width="140">44.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steellarge/narayanisteels/NS10" style="text-decoration:none;color:#333333">Narayani Steels</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE715T01015','BSE','540080');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Narayani Steels on BSE</span></li><li><span>Only Sellers in Narayani Steels on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">34.25</td>
                    <td align="right" width="130">36.50</td>
                    <td align="right" width="140">2.25</td>
                    <td align="right" width="140">6.57</td>
                    <td align="right" width="140">36.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/nirajcementstructurals/NCS02" style="text-decoration:none;color:#333333">Niraj Cement</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE368I01016','BSE','532986');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Niraj Cement Structurals: Outcome of board meeting</span></a></li><li><a href="javascript:void(0)"><span>Niraj Cement: Outcome of AGM</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/nirajcementstructurals/notices/NCS02" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Niraj Cement on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.00</td>
                    <td align="right" width="130">30.90</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">6.55</td>
                    <td align="right" width="140">30.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/jyotiresinsadhesives/JRA" style="text-decoration:none;color:#333333">Jyoti Resins</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE577D01013','BSE','514448');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Jyoti Resin: Outcome of AGM</span></a></li><li><a href="javascript:void(0)"><span>Jyoti Resins' AGM on September 30, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/jyotiresinsadhesives/notices/JRA" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Jyoti Resins closes above 150-Day Moving Average of 166.75 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">169.00</td>
                    <td align="right" width="130">180.00</td>
                    <td align="right" width="140">11.00</td>
                    <td align="right" width="140">6.51</td>
                    <td align="right" width="140">180.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/retail/futurelifestylefashions/FLF01" style="text-decoration:none;color:#333333">Future Life</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE452O01016','BSE','536507');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Future Life has hit 52wk low of Rs 299.80 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">324.45</td>
                    <td align="right" width="130">344.95</td>
                    <td align="right" width="140">20.50</td>
                    <td align="right" width="140">6.32</td>
                    <td align="right" width="140">344.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/kpenergy/KEL04" style="text-decoration:none;color:#333333">K.P. Energy </a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE127T01013','BSE','539686');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>K.P. Energy  closes above 50-Day Moving Average of 121.41 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">127.00</td>
                    <td align="right" width="130">135.00</td>
                    <td align="right" width="140">8.00</td>
                    <td align="right" width="140">6.30</td>
                    <td align="right" width="140">135.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/auto23wheelers/scootersindia/SI09" style="text-decoration:none;color:#333333">Scooters India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE959E01011','BSE','505141');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in Scooters India on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">22.45</td>
                    <td align="right" width="130">23.85</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">6.24</td>
                    <td align="right" width="140">23.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/texmacorailengineering/TRE" style="text-decoration:none;color:#333333">Texmaco Rail</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE621L01012','BSE','533326');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Texmaco Rail closes above 50-Day Moving Average of 38.52 today.</span></li><li><span>Only Buyers in Texmaco Rail on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">24.10</td>
                    <td align="right" width="130">25.60</td>
                    <td align="right" width="140">1.50</td>
                    <td align="right" width="140">6.22</td>
                    <td align="right" width="140">25.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/sobha/SD6" style="text-decoration:none;color:#333333">Sobha</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE671H01015','BSE','532784');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sobha Block Deal on NSE||Qty: 115,000||Deal Price: 436.00||Value (cr): 5.01||Time: 09:47am</span></li><li><span>Sobha Block Deal on NSE||Qty: 115,000||Deal Price: 436.00||Value (cr): 5.01||Time: 09:47am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">308.00</td>
                    <td align="right" width="130">327.00</td>
                    <td align="right" width="140">19.00</td>
                    <td align="right" width="140">6.17</td>
                    <td align="right" width="140">327.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steelcrhrstrips/rishabhdighasteelalliedproducts/RDS" style="text-decoration:none;color:#333333">Rishabh Digha</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE864D01015','BSE','531539');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rishabh Digha closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">20.30</td>
                    <td align="right" width="130">21.50</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">5.91</td>
                    <td align="right" width="140">21.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cablespowerothers/keiindustries/KEI" style="text-decoration:none;color:#333333">KEI Industries</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE878B01027','BSE','517569');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KEI Industries closes above 150-Day,200-Day Moving Average today.</span></li><li><span>KEI Industries closes below 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">491.35</td>
                    <td align="right" width="130">520.20</td>
                    <td align="right" width="140">28.85</td>
                    <td align="right" width="140">5.87</td>
                    <td align="right" width="140">520.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/dutronpolymers/DP08" style="text-decoration:none;color:#333333">Dutron Polymers</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE940C01015','BSE','517437');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Dutron Polymers has hit 52wk low of Rs 103.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">98.05</td>
                    <td align="right" width="130">103.80</td>
                    <td align="right" width="140">5.75</td>
                    <td align="right" width="140">5.86</td>
                    <td align="right" width="140">103.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/januscorporationlimited/JANUS54292" style="text-decoration:none;color:#333333">JCL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE04OV01018','BSE','542924');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in JCL on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">52.10</td>
                    <td align="right" width="130">55.00</td>
                    <td align="right" width="140">2.90</td>
                    <td align="right" width="140">5.57</td>
                    <td align="right" width="140">55.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/hindusthanurbaninfrastructurelimited/HUI" style="text-decoration:none;color:#333333">Hindusthan Urba</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE799B01017','BSE','539984');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Hindusthan Urban Infrastructure's EGM on November 22, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/hindusthanurbaninfrastructurelimited/notices/HUI" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Hindusthan Urba closes below  its 30-Day,50-Day,150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">645.00</td>
                    <td align="right" width="130">679.90</td>
                    <td align="right" width="140">34.90</td>
                    <td align="right" width="140">5.41</td>
                    <td align="right" width="140">679.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/mediaentertainment/tvtodaynetwork/TVT" style="text-decoration:none;color:#333333">TV TodayNetwork</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE038F01029','BSE','532515');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>TV TodayNetwork closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">216.35</td>
                    <td align="right" width="130">227.90</td>
                    <td align="right" width="140">11.55</td>
                    <td align="right" width="140">5.34</td>
                    <td align="right" width="140">227.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/pncinfratech/PI26" style="text-decoration:none;color:#333333">PNC Infratech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE195J01029','BSE','539150');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PNC Infratech closes below 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">175.00</td>
                    <td align="right" width="130">184.00</td>
                    <td align="right" width="140">9.00</td>
                    <td align="right" width="140">5.14</td>
                    <td align="right" width="140">184.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/weizmannforex/WF02" style="text-decoration:none;color:#333333">Weizmann Forex</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE726L01019','BSE','533452');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Weizmann Forex closes above 30-Day Moving Average of 375.66 today.</span></li><li><span>Only Buyers in Weizmann Forex on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">333.05</td>
                    <td align="right" width="130">350.00</td>
                    <td align="right" width="140">16.95</td>
                    <td align="right" width="140">5.09</td>
                    <td align="right" width="140">350.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/iiflsecuritieslimited/IIFLS54277" style="text-decoration:none;color:#333333">ISL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE489L01022','BSE','542773');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in ISL on BSE</span></li><li><span>Only Sellers in ISL on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">45.20</td>
                    <td align="right" width="130">47.50</td>
                    <td align="right" width="140">2.30</td>
                    <td align="right" width="140">5.09</td>
                    <td align="right" width="140">47.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/texmacoinfrastructureholdings/T02" style="text-decoration:none;color:#333333">Texmaco Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE435C01024','BSE','505400');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Texmaco Infra closes below 200-Day Moving Average of 44.96 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">39.00</td>
                    <td align="right" width="130">40.95</td>
                    <td align="right" width="140">1.95</td>
                    <td align="right" width="140">5.00</td>
                    <td align="right" width="140">40.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/trading/satindustries/SIL15" style="text-decoration:none;color:#333333">Sat Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE065D01027','BSE','511076');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sat Ind POM on Nov 18, 2019||Announcement date: Oct 15, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">24.15</td>
                    <td align="right" width="130">25.35</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">4.97</td>
                    <td align="right" width="140">25.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/primesecurities/PS" style="text-decoration:none;color:#333333">Prime Sec</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE032B01021','BSE','500337');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Prime Sec closes above 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">36.20</td>
                    <td align="right" width="130">38.00</td>
                    <td align="right" width="140">1.80</td>
                    <td align="right" width="140">4.97</td>
                    <td align="right" width="140">38.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steelmediumsmall/bharatwireropes/BWR01" style="text-decoration:none;color:#333333">Bharat Wire Rop</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE316L01019','BSE','539799');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Bharat Wire Rop closes above  its 30-Day,50-Day,150-Day Moving Average today.</span></li><li><span>Only Buyers in Bharat Wire Rop on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">25.30</td>
                    <td align="right" width="130">26.50</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">4.74</td>
                    <td align="right" width="140">26.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/ramkyinfrastructure/RI12" style="text-decoration:none;color:#333333">Ramky Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE874I01013','BSE','533262');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ramky Infra closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">26.75</td>
                    <td align="right" width="130">28.00</td>
                    <td align="right" width="140">1.25</td>
                    <td align="right" width="140">4.67</td>
                    <td align="right" width="140">28.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/transportlogistics/agarwalindustrialcorporation/AIC03" style="text-decoration:none;color:#333333">Agarwal Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE204E01012','BSE','531921');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Agarwal Ind has hit 52wk low of Rs 68.00 on NSE</span></li><li><span>Agarwal Ind has hit 52wk low of Rs 68.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">72.05</td>
                    <td align="right" width="130">75.35</td>
                    <td align="right" width="140">3.30</td>
                    <td align="right" width="140">4.58</td>
                    <td align="right" width="140">75.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/leadingleasingfinanceandinvestmentcompany/LLF" style="text-decoration:none;color:#333333">Leading Leasing</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE715Q01011','BSE','540360');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Leading Leasing Finance And Investment Company's board meeting on November 13, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/leadingleasingfinanceinvestmentcompany/notices/LLF" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Leading Leasing on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">128.20</td>
                    <td align="right" width="130">133.90</td>
                    <td align="right" width="140">5.70</td>
                    <td align="right" width="140">4.45</td>
                    <td align="right" width="140">133.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/personalcare/godrejindustries/GI23" style="text-decoration:none;color:#333333">Godrej Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE233A01035','BSE','500164');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Godrej Ind closes above 30-Day Moving Average of 431.52 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">410.60</td>
                    <td align="right" width="130">428.75</td>
                    <td align="right" width="140">18.15</td>
                    <td align="right" width="140">4.42</td>
                    <td align="right" width="140">428.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/trading/apollotricoattubes/PIF03" style="text-decoration:none;color:#333333">Apollo Tricoat </a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE919P01029','BSE','538566');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Apollo Tricoat  closes above 50-Day Moving Average of 275.61 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">431.00</td>
                    <td align="right" width="130">450.00</td>
                    <td align="right" width="140">19.00</td>
                    <td align="right" width="140">4.41</td>
                    <td align="right" width="140">450.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/mangalorechemicalsfertilisers/MCF01" style="text-decoration:none;color:#333333">Mangalore Chem</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE558B01017','BSE','530011');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mangalore Chem closes above 50-Day Moving Average of 31.63 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.75</td>
                    <td align="right" width="130">31.05</td>
                    <td align="right" width="140">1.30</td>
                    <td align="right" width="140">4.37</td>
                    <td align="right" width="140">31.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/shivalikrasayan/SR9" style="text-decoration:none;color:#333333">Shivalik Rasa</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE788J01021','BSE','539148');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Shivalik Rasa on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">270.00</td>
                    <td align="right" width="130">281.80</td>
                    <td align="right" width="140">11.80</td>
                    <td align="right" width="140">4.37</td>
                    <td align="right" width="140">281.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/tataelxsi/TE" style="text-decoration:none;color:#333333">Tata Elxsi</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE670A01012','BSE','500408');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Tata Elxsi closes above 30-Day Moving Average of 989.53 today.</span></li><li><span>Tata Elxsi closes above 50-Day Moving Average of 936.95 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">998.90</td>
                    <td align="right" width="130">1,041.65</td>
                    <td align="right" width="140">42.75</td>
                    <td align="right" width="140">4.28</td>
                    <td align="right" width="140">1,041.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/naharcapitalfinancialservices/NCF" style="text-decoration:none;color:#333333">Nahar Capital</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE049I01012','BSE','532952');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nahar Capital closes below 50-Day Moving Average of 74.29 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">67.05</td>
                    <td align="right" width="130">69.90</td>
                    <td align="right" width="140">2.85</td>
                    <td align="right" width="140">4.25</td>
                    <td align="right" width="140">69.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/tokyoplastinternational/TPI01" style="text-decoration:none;color:#333333">Tokyo Plast</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE932C01012','BSE','500418');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Tokyo Plast closes above 150-Day Moving Average of 62.31 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">61.40</td>
                    <td align="right" width="130">64.00</td>
                    <td align="right" width="140">2.60</td>
                    <td align="right" width="140">4.23</td>
                    <td align="right" width="140">64.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesspinningcottonblended/rajapalayammills/RM06" style="text-decoration:none;color:#333333">Rajapalayam</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE296E01026','BSE','532503');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Rajapalayam Mills: Outcome of board meeting</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/rajapalayammills/notices/RM06" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rajapalayam AGM on Aug 14, 2019||Announcement date: Jul 16, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">681.60</td>
                    <td align="right" width="130">710.00</td>
                    <td align="right" width="140">28.40</td>
                    <td align="right" width="140">4.17</td>
                    <td align="right" width="140">710.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/diamondcuttingjewellerypreciousmetals/zodiacjrdmkj/ZJR" style="text-decoration:none;color:#333333">Zodiac JRD-MKJ</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE077B01018','BSE','512587');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Zodiac JRD-MKJ closes above 30-Day Moving Average of 29.31 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">30.00</td>
                    <td align="right" width="130">31.25</td>
                    <td align="right" width="140">1.25</td>
                    <td align="right" width="140">4.17</td>
                    <td align="right" width="140">31.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/packaging/everestkantocylinder/EKC" style="text-decoration:none;color:#333333">Everest Kanto</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE184H01027','BSE','532684');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Everest Kanto closes below 200-Day Moving Average of 24.51 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">20.65</td>
                    <td align="right" width="130">21.50</td>
                    <td align="right" width="140">0.85</td>
                    <td align="right" width="140">4.12</td>
                    <td align="right" width="140">21.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powertransmissionequipment/kalpatarupowertransmission/KPT" style="text-decoration:none;color:#333333">Kalpataru Power</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE220B01022','BSE','522287');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kalpataru Power has hit 52wk low of Rs 345.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">324.45</td>
                    <td align="right" width="130">337.65</td>
                    <td align="right" width="140">13.20</td>
                    <td align="right" width="140">4.07</td>
                    <td align="right" width="140">337.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financegeneral/sastasundarventures/MFS" style="text-decoration:none;color:#333333">Sasta Sundar</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE019J01013','BSE','533259');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sasta Sundar closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">67.10</td>
                    <td align="right" width="130">69.80</td>
                    <td align="right" width="140">2.70</td>
                    <td align="right" width="140">4.02</td>
                    <td align="right" width="140">69.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/ajantapharma/AP22" style="text-decoration:none;color:#333333">Ajanta Pharma</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE031B01049','BSE','532331');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ajanta Pharma closes above  its 30-Day,50-Day,150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,416.30</td>
                    <td align="right" width="130">1,473.20</td>
                    <td align="right" width="140">56.90</td>
                    <td align="right" width="140">4.02</td>
                    <td align="right" width="140">1,473.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/cescventureslimited/CESCV54233" style="text-decoration:none;color:#333333">CVL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE425Y01011','BSE','542333');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>CVL has hit 52wk low of Rs 268.00 on NSE</span></li><li><span>CVL has hit 52wk low of Rs 270.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">274.40</td>
                    <td align="right" width="130">285.30</td>
                    <td align="right" width="140">10.90</td>
                    <td align="right" width="140">3.97</td>
                    <td align="right" width="140">285.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/indiabullsrealestate/IRE01" style="text-decoration:none;color:#333333">Indiabulls Real</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE069I01010','BSE','532832');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Indiabulls Real closes above 150-Day Moving Average of 72.22 today.</span></li><li><span>Only Buyers in Indiabulls Real on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">72.00</td>
                    <td align="right" width="130">74.85</td>
                    <td align="right" width="140">2.85</td>
                    <td align="right" width="140">3.96</td>
                    <td align="right" width="140">74.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/elnettechnologies/ET03" style="text-decoration:none;color:#333333">Elnet Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE033C01019','BSE','517477');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Elnet Technologies' nominee director K. Padmanaban resigns</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/elnettechnologies/notices/ET03" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Elnet Tech closes below  its 30-Day,50-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">101.00</td>
                    <td align="right" width="130">105.00</td>
                    <td align="right" width="140">4.00</td>
                    <td align="right" width="140">3.96</td>
                    <td align="right" width="140">105.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/resonancespecialities/RS20" style="text-decoration:none;color:#333333">Resonance</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE486D01017','BSE','524218');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Resonance on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">51.00</td>
                    <td align="right" width="130">53.00</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">3.92</td>
                    <td align="right" width="140">53.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/mahindraholidaysresortsindia/MHR" style="text-decoration:none;color:#333333">Mahindra Holida</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE998I01010','BSE','533088');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mahindra Holida closes below 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">215.00</td>
                    <td align="right" width="130">223.35</td>
                    <td align="right" width="140">8.35</td>
                    <td align="right" width="140">3.88</td>
                    <td align="right" width="140">223.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/capaciteinfraprojects/CI19" style="text-decoration:none;color:#333333">Capacite Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE264T01014','BSE','540710');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Capacite Infra has hit 52wk low of Rs 154.50 on NSE</span></li><li><span>Capacite Infra has hit 52wk low of Rs 155.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">149.70</td>
                    <td align="right" width="130">155.50</td>
                    <td align="right" width="140">5.80</td>
                    <td align="right" width="140">3.87</td>
                    <td align="right" width="140">155.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/prakashpipeslimited/PPL54268" style="text-decoration:none;color:#333333">PPL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE050001010','BSE','542684');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PPL closes above 30-Day Moving Average of 69.96 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">52.95</td>
                    <td align="right" width="130">55.00</td>
                    <td align="right" width="140">2.05</td>
                    <td align="right" width="140">3.87</td>
                    <td align="right" width="140">55.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/birlasoft/KPI02" style="text-decoration:none;color:#333333">Birlasoft</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE836A01035','BSE','532400');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Birlasoft Dividend||Interim Dividend 50.00%||Announcement date: Jan 27, 2020||Record date: Feb 10, 2020||Ex-Div: Feb 07, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">89.65</td>
                    <td align="right" width="130">93.05</td>
                    <td align="right" width="140">3.40</td>
                    <td align="right" width="140">3.79</td>
                    <td align="right" width="140">93.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/zimlaboratorieslimited/ZIMLA54140" style="text-decoration:none;color:#333333">ZIM Laboratorie</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE518E01015','BSE','541400');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>ZIM Laboratorie has hit 52wk low of Rs 57.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">61.00</td>
                    <td align="right" width="130">63.30</td>
                    <td align="right" width="140">2.30</td>
                    <td align="right" width="140">3.77</td>
                    <td align="right" width="140">63.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/mediaentertainment/hindustanmediaventures/HMV" style="text-decoration:none;color:#333333">Hindustan Media</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE871K01015','BSE','533217');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Hindustan Media has hit 52wk low of Rs 60.35 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">60.05</td>
                    <td align="right" width="130">62.30</td>
                    <td align="right" width="140">2.25</td>
                    <td align="right" width="140">3.75</td>
                    <td align="right" width="140">62.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/welspuncorp/WGS" style="text-decoration:none;color:#333333">Welspun Corp</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE191B01025','BSE','532144');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Welspun Corp Dividend||Interim Dividend 200.00%||Announcement date: Feb 04, 2020||Record date: Feb 13, 2020||Ex-Div: Feb 12, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">168.60</td>
                    <td align="right" width="130">174.85</td>
                    <td align="right" width="140">6.25</td>
                    <td align="right" width="140">3.71</td>
                    <td align="right" width="140">174.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/avantel/A19" style="text-decoration:none;color:#333333">Avantel</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE005B01019','BSE','532406');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Avantel on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">254.00</td>
                    <td align="right" width="130">263.40</td>
                    <td align="right" width="140">9.40</td>
                    <td align="right" width="140">3.70</td>
                    <td align="right" width="140">263.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesreadymadeapparels/kprmill/M15" style="text-decoration:none;color:#333333">KPR Mill</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE930H01023','BSE','532889');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KPR Mill closes above 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">578.60</td>
                    <td align="right" width="130">599.90</td>
                    <td align="right" width="140">21.30</td>
                    <td align="right" width="140">3.68</td>
                    <td align="right" width="140">599.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/nhpc/N07" style="text-decoration:none;color:#333333">NHPC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE848E01016','BSE','533098');"></span><div class="MT5"></div></td>
                    <td align="right" width="130">22.00</td>
                    <td align="right" width="130">22.80</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">3.64</td>
                    <td align="right" width="140">22.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeleasinghirepurchase/mangalcreditfincorp/TML" style="text-decoration:none;color:#333333">Mangal Credit</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE545L01039','BSE','505850');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mangal Credit AGM on Sep 30, 2019||Announcement date: Aug 14, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">40.00</td>
                    <td align="right" width="130">41.45</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">3.63</td>
                    <td align="right" width="140">41.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesmachinery/integraengineeringindia/SE06" style="text-decoration:none;color:#333333">Integra Engg</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE984B01023','BSE','505358');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Integra Engg AGM on Jul 18, 2019||Announcement date: Jun 14, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">31.90</td>
                    <td align="right" width="130">33.00</td>
                    <td align="right" width="140">1.10</td>
                    <td align="right" width="140">3.45</td>
                    <td align="right" width="140">33.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textileswoollenworsted/prakashwoollensyntheticmills/PWM" style="text-decoration:none;color:#333333">Prakash Woollen</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE523I01016','BSE','531437');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Prakash Woollen has hit 52wk low of Rs 16.60 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">21.80</td>
                    <td align="right" width="130">22.55</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">3.44</td>
                    <td align="right" width="140">22.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/okplayindia/OKP" style="text-decoration:none;color:#333333">OK Play</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE870B01016','BSE','526415');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>OK Play India - Outcome of board meeting</span></a></li><li><a href="javascript:void(0)"><span>OK Play India's board meeting on December 14, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/okplayindia/notices/OKP" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in OK Play on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">38.10</td>
                    <td align="right" width="130">39.40</td>
                    <td align="right" width="140">1.30</td>
                    <td align="right" width="140">3.41</td>
                    <td align="right" width="140">39.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financehousing/srghousingfinance/SHF02" style="text-decoration:none;color:#333333">SRG Housing Fin</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE559N01010','BSE','534680');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>SRG Housing Fin closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">74.00</td>
                    <td align="right" width="130">76.50</td>
                    <td align="right" width="140">2.50</td>
                    <td align="right" width="140">3.38</td>
                    <td align="right" width="140">76.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/keltechenergies/KEL03" style="text-decoration:none;color:#333333">KELTECH Energ</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE881E01017','BSE','506528');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KELTECH Energ closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">642.50</td>
                    <td align="right" width="130">664.00</td>
                    <td align="right" width="140">21.50</td>
                    <td align="right" width="140">3.35</td>
                    <td align="right" width="140">664.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/gandhispecialtubes/GST" style="text-decoration:none;color:#333333">Gandhi Spl Tube</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE524B01027','BSE','513108');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Gandhi Spl Tube has hit 52wk low of Rs 217.05 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">234.50</td>
                    <td align="right" width="130">242.30</td>
                    <td align="right" width="140">7.80</td>
                    <td align="right" width="140">3.33</td>
                    <td align="right" width="140">242.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/puravankara/PP01" style="text-decoration:none;color:#333333">Puravankara</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE323I01011','BSE','532891');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Puravankara closes below 50-Day Moving Average of 59.89 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">50.35</td>
                    <td align="right" width="130">52.00</td>
                    <td align="right" width="140">1.65</td>
                    <td align="right" width="140">3.28</td>
                    <td align="right" width="140">52.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeleasinghirepurchase/im+capitals/BCA" style="text-decoration:none;color:#333333">IM+ Capitals</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE417D01012','BSE','511628');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>IM+ Capitals closes above 30-Day Moving Average of 22.92 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">19.80</td>
                    <td align="right" width="130">20.45</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">3.28</td>
                    <td align="right" width="140">20.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/kanoriachemicalsindustries/KCI01" style="text-decoration:none;color:#333333">Kanoria Chem</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE138C01024','BSE','506525');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kanoria Chem closes above 30-Day,150-Day Moving Average today.</span></li><li><span>Kanoria Chem closes above 30-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">36.60</td>
                    <td align="right" width="130">37.80</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">3.28</td>
                    <td align="right" width="140">37.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/printingstationery/tcplpackaging/TCP01" style="text-decoration:none;color:#333333">TCPL Packaging</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE822C01015','BSE','523301');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>TCPL Packaging closes below 150-Day Moving Average of 279.69 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">260.00</td>
                    <td align="right" width="130">268.50</td>
                    <td align="right" width="140">8.50</td>
                    <td align="right" width="140">3.27</td>
                    <td align="right" width="140">268.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/akzonobelindia/ICI" style="text-decoration:none;color:#333333">Akzo Nobel</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE133A01011','BSE','500710');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Akzo Nobel Block Deal on NSE||Qty: 25,000||Deal Price: 2,113.00||Value (cr): 5.28||Time: 10:08am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,377.00</td>
                    <td align="right" width="130">2,454.55</td>
                    <td align="right" width="140">77.55</td>
                    <td align="right" width="140">3.26</td>
                    <td align="right" width="140">2,454.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeleasinghirepurchase/pioneerinvestcorp/PI12" style="text-decoration:none;color:#333333">Pioneer Invest</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE746D01014','BSE','507864');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Pioneer Invest AGM on Sep 24, 2019||Announcement date: Aug 23, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">34.50</td>
                    <td align="right" width="130">35.60</td>
                    <td align="right" width="140">1.10</td>
                    <td align="right" width="140">3.19</td>
                    <td align="right" width="140">35.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cigarettes/goldentobacco/GT09" style="text-decoration:none;color:#333333">Golden Tobacco</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE973A01010','BSE','500151');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Golden Tobacco closes below 30-Day Moving Average of 27.56 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.60</td>
                    <td align="right" width="130">24.35</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">3.18</td>
                    <td align="right" width="140">24.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/muthootcapitalservices/MCS02" style="text-decoration:none;color:#333333">Muthoot Cap</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE296G01013','BSE','511766');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Muthoot Cap closes below 150-Day Moving Average of 516.66 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">498.00</td>
                    <td align="right" width="130">513.85</td>
                    <td align="right" width="140">15.85</td>
                    <td align="right" width="140">3.18</td>
                    <td align="right" width="140">513.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cablestelephone/sterlitetechnologies/ST20" style="text-decoration:none;color:#333333">Sterlite Techno</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE089C01029','BSE','532374');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sterlite Techno closes below 50-Day Moving Average of 122.37 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">89.85</td>
                    <td align="right" width="130">92.70</td>
                    <td align="right" width="140">2.85</td>
                    <td align="right" width="140">3.17</td>
                    <td align="right" width="140">92.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/dyespigments/polson/P08" style="text-decoration:none;color:#333333">Polson</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE339F01021','BSE','507645');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Polson has hit 52wk low of Rs 7,230.05 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">8,612.55</td>
                    <td align="right" width="130">8,879.95</td>
                    <td align="right" width="140">267.40</td>
                    <td align="right" width="140">3.10</td>
                    <td align="right" width="140">8,879.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/trading/uniphosenterprises/UE" style="text-decoration:none;color:#333333">Uniphos Ent</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE037A01022','BSE','500429');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Uniphos Ent closes above 50-Day Moving Average of 67.61 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">66.00</td>
                    <td align="right" width="130">68.00</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">3.03</td>
                    <td align="right" width="140">68.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/saksoft/S12" style="text-decoration:none;color:#333333">Saksoft</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE667G01015','BSE','590051');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Saksoft closes below 50-Day Moving Average of 217.90 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">189.10</td>
                    <td align="right" width="130">194.80</td>
                    <td align="right" width="140">5.70</td>
                    <td align="right" width="140">3.01</td>
                    <td align="right" width="140">194.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/titanbiotech/TBT" style="text-decoration:none;color:#333333">Titan Bio-Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE150C01011','BSE','524717');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Titan Bio-Tech's board meeting held on January 03, 2018</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/titanbio-tech/notices/TBT" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Titan Bio-Tech closes above 30-Day,50-Day Moving Average today.</span></li><li><span>Only Buyers in Titan Bio-Tech on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">57.10</td>
                    <td align="right" width="130">58.80</td>
                    <td align="right" width="140">1.70</td>
                    <td align="right" width="140">2.98</td>
                    <td align="right" width="140">58.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/vanaspatioils/ivp/IVP" style="text-decoration:none;color:#333333">IVP</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE043C01018','BSE','507580');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>IVP closes above 30-Day Moving Average of 48.82 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">47.10</td>
                    <td align="right" width="130">48.50</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">2.97</td>
                    <td align="right" width="140">48.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financegeneral/masfinancialservices/MFS09" style="text-decoration:none;color:#333333">MAS Financial S</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE348L01012','BSE','540749');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>MAS Financial S closes above 30-Day Moving Average of 1037.94 today.</span></li><li><span>MAS Financial S closes below 30-Day Moving Average of 1033.00 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,039.50</td>
                    <td align="right" width="130">1,070.30</td>
                    <td align="right" width="140">30.80</td>
                    <td align="right" width="140">2.96</td>
                    <td align="right" width="140">1,070.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/nationalplasticindustries/NPI" style="text-decoration:none;color:#333333">National Plasti</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE233D01013','BSE','526616');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>National Plastic Industries' board meeting held on November 8, 2017</span></a></li><li><a href="javascript:void(0)"><span>National Plastic Industries: Outcome of AGM</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/nationalplasticindustries/notices/NPI" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>National Plasti has hit 52wk low of Rs 21.50 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">22.00</td>
                    <td align="right" width="130">22.65</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">2.95</td>
                    <td align="right" width="140">22.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/mediaentertainment/jagranprakashan/JP12" style="text-decoration:none;color:#333333">JagranPrakashan</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE199G01027','BSE','532705');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>JagranPrakashan closes above 150-Day Moving Average of 68.48 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">57.80</td>
                    <td align="right" width="130">59.50</td>
                    <td align="right" width="140">1.70</td>
                    <td align="right" width="140">2.94</td>
                    <td align="right" width="140">59.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electrodesgraphite/gee/GEE02" style="text-decoration:none;color:#333333">GEE</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE064H01021','BSE','504028');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>GEE closes above 50-Day Moving Average of 23.71 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">31.00</td>
                    <td align="right" width="130">31.90</td>
                    <td align="right" width="140">0.90</td>
                    <td align="right" width="140">2.90</td>
                    <td align="right" width="140">31.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/breweriesdistilleries/radicokhaitan/RK01" style="text-decoration:none;color:#333333">Radico Khaitan</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE944F01028','BSE','532497');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Radico Khaitan packs a punch with Q3 premium play</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">390.25</td>
                    <td align="right" width="130">401.15</td>
                    <td align="right" width="140">10.90</td>
                    <td align="right" width="140">2.79</td>
                    <td align="right" width="140">401.15</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pesticidesagrochemicals/piindustries/PII" style="text-decoration:none;color:#333333">PI Industries</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE603J01030','BSE','523642');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PI Industries closes above 30-Day Moving Average of 1537.77 today.</span></li><li><span>PI Industries closes above 30-Day Moving Average of 1531.16 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,535.30</td>
                    <td align="right" width="130">1,578.00</td>
                    <td align="right" width="140">42.70</td>
                    <td align="right" width="140">2.78</td>
                    <td align="right" width="140">1,578.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electrodesgraphite/graphiteindia/GI13" style="text-decoration:none;color:#333333">Graphite India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE371A01025','BSE','509488');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Graphite India has hit 52wk low of Rs 226.10 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">229.65</td>
                    <td align="right" width="130">236.00</td>
                    <td align="right" width="140">6.35</td>
                    <td align="right" width="140">2.77</td>
                    <td align="right" width="140">236.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/vivobiotech/VB04" style="text-decoration:none;color:#333333">Vivo Biotech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE380K01017','BSE','511509');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Vivo Biotech's board meeting on September 13, 2017</span></a></li><li><a href="javascript:void(0)"><span>Vivo Biotech's board meeting on August 28, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/vivobiotech/notices/VB04" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Vivo Biotech closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.70</td>
                    <td align="right" width="130">24.35</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">2.74</td>
                    <td align="right" width="140">24.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/agritechindia/ATI02" style="text-decoration:none;color:#333333">Agri-Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE449G01018','BSE','537292');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Agri-Tech has hit 52wk low of Rs 37.25 on NSE</span></li><li><span>Agri-Tech has hit 52wk low of Rs 38.10 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">38.50</td>
                    <td align="right" width="130">39.55</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">2.73</td>
                    <td align="right" width="140">39.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cementproductsbuildingmaterials/sanghiindustries/SI04" style="text-decoration:none;color:#333333">Sanghi Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE999B01013','BSE','526521');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sanghi Ind Block Deal on BSE||Qty: 650,000||Deal Price: 31.05||Value (cr): 2.02||Time: 09:16am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">31.15</td>
                    <td align="right" width="130">32.00</td>
                    <td align="right" width="140">0.85</td>
                    <td align="right" width="140">2.73</td>
                    <td align="right" width="140">32.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/sugar/bannariammansugars/BS07" style="text-decoration:none;color:#333333">Bannariamman</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE459A01010','BSE','500041');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Bannariamman closes below 30-Day Moving Average of 1455.25 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,190.00</td>
                    <td align="right" width="130">1,222.00</td>
                    <td align="right" width="140">32.00</td>
                    <td align="right" width="140">2.69</td>
                    <td align="right" width="140">1,222.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cementproductsbuildingmaterials/orientrefractories/OR01" style="text-decoration:none;color:#333333">Orient Refract</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE743M01012','BSE','534076');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Orient Refract closes above 30-Day Moving Average of 216.91 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">225.00</td>
                    <td align="right" width="130">231.05</td>
                    <td align="right" width="140">6.05</td>
                    <td align="right" width="140">2.69</td>
                    <td align="right" width="140">231.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/kalyaniinvestmentcompany/KIC04" style="text-decoration:none;color:#333333">Kalyani Invest</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE029L01018','BSE','533302');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kalyani Invest closes below 50-Day Moving Average of 1728.88 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,462.75</td>
                    <td align="right" width="130">1,502.00</td>
                    <td align="right" width="140">39.25</td>
                    <td align="right" width="140">2.68</td>
                    <td align="right" width="140">1,502.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/kavitindustries/JHP" style="text-decoration:none;color:#333333">Kavit Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE313M01014','BSE','524444');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Kavit Ind: Outcome of AGM</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/kavitindustries/notices/JHP" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kavit Ind closes above 50-Day Moving Average of 44.40 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">108.50</td>
                    <td align="right" width="130">111.40</td>
                    <td align="right" width="140">2.90</td>
                    <td align="right" width="140">2.67</td>
                    <td align="right" width="140">111.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/castingsforgings/investmentprecisioncastings/IPC01" style="text-decoration:none;color:#333333">Invest and Prec</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE155E01016','BSE','504786');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Invest and Prec AGM on Sep 26, 2019||Announcement date: Aug 21, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">195.00</td>
                    <td align="right" width="130">200.00</td>
                    <td align="right" width="140">5.00</td>
                    <td align="right" width="140">2.56</td>
                    <td align="right" width="140">200.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/coromandelinternational/CI45" style="text-decoration:none;color:#333333">Coromandel Int</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE169A01031','BSE','506395');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Coromandel Int closes above 30-Day Moving Average of 618.28 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">612.25</td>
                    <td align="right" width="130">627.95</td>
                    <td align="right" width="140">15.70</td>
                    <td align="right" width="140">2.56</td>
                    <td align="right" width="140">627.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cablestelephone/vindhyatelelink/VT03" style="text-decoration:none;color:#333333">Vindhya Telelin</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE707A01012','BSE','517015');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Vindhya Telelin closes above 50-Day Moving Average of 903.90 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">759.25</td>
                    <td align="right" width="130">778.30</td>
                    <td align="right" width="140">19.05</td>
                    <td align="right" width="140">2.51</td>
                    <td align="right" width="140">778.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hospitalsmedicalservices/lotuseyecarehospital/LEC01" style="text-decoration:none;color:#333333">Lotus Eye Care</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE947I01017','BSE','532998');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Lotus Eye Care closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">25.95</td>
                    <td align="right" width="130">26.60</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">2.50</td>
                    <td align="right" width="140">26.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesgeneral/jindalworldwide/JW01" style="text-decoration:none;color:#333333">Jindal Worldwid</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE247D01039','BSE','531543');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Jindal Worldwid closes below  its 30-Day,50-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">57.95</td>
                    <td align="right" width="130">59.40</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">2.50</td>
                    <td align="right" width="140">59.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financegeneral/akcapitalservices/AKC01" style="text-decoration:none;color:#333333">A.K.Capital Ser</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE701G01012','BSE','530499');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>A.K.Capital Services: Outcome of Board Meeting</span></a></li><li><a href="javascript:void(0)"><span>A.K.Capital Services' board meeting on November 11, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/akcapitalservices/notices/AKC01" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>A.K.Capital Ser has hit 52wk low of Rs 227.00 on BSE</span></li><li><span>A.K.Capital Ser has hit 52wk low of Rs 227.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">232.00</td>
                    <td align="right" width="130">237.80</td>
                    <td align="right" width="140">5.80</td>
                    <td align="right" width="140">2.50</td>
                    <td align="right" width="140">237.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/nbccindia/NBC01" style="text-decoration:none;color:#333333">NBCC (India)</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE095N01031','BSE','534309');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/nbcc-bags-order-worth-rs-65crbhel_13541981.html" title="NBCC bags order worth Rs 65cr from BHEL"><span>NBCC bags order worth Rs 65cr from BHEL</span></a><em>Mar 02, 12:30</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/nbccindia/news/NBC01" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">26.55</td>
                    <td align="right" width="130">27.20</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">2.45</td>
                    <td align="right" width="140">27.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/castingsforgings/aliconcastalloy/EC06" style="text-decoration:none;color:#333333">Alicon Castallo</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE062D01024','BSE','531147');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Alicon Castalloy Limited</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/aliconcastalloy/notices/EC06" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Alicon Castallo has hit 52wk low of Rs 281.05 on BSE</span></li><li><span>Alicon Castallo has hit 52wk low of Rs 276.20 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">284.05</td>
                    <td align="right" width="130">291.00</td>
                    <td align="right" width="140">6.95</td>
                    <td align="right" width="140">2.45</td>
                    <td align="right" width="140">291.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/jubilantlifesciences/JO03" style="text-decoration:none;color:#333333">Jubilant Life</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE700A01033','BSE','530019');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Jubilant Life closes below 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">490.10</td>
                    <td align="right" width="130">502.00</td>
                    <td align="right" width="140">11.90</td>
                    <td align="right" width="140">2.43</td>
                    <td align="right" width="140">502.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/confidencepetroleum/CP10" style="text-decoration:none;color:#333333">ConfidencePetro</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE552D01024','BSE','526829');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>ConfidencePetro EGM on Feb 04, 2020||Announcement date: Jan 09, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.00</td>
                    <td align="right" width="130">23.55</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">2.39</td>
                    <td align="right" width="140">23.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/natcopharma/NP07" style="text-decoration:none;color:#333333">Natco Pharma</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE987B01026','BSE','524816');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Natco Pharma closes below 30-Day Moving Average of 652.73 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">609.90</td>
                    <td align="right" width="130">624.45</td>
                    <td align="right" width="140">14.55</td>
                    <td align="right" width="140">2.39</td>
                    <td align="right" width="140">624.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/kpittechnologies/KPITT54265" style="text-decoration:none;color:#333333">KT</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE04I401011','BSE','542651');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KT Dividend||Final Dividend 5.50%||Announcement date: Jan 29, 2020||Record date: Feb 18, 2020||Ex-Div: Feb 17, 2020</span></li><li><span>KT Dividend||Interim Dividend 5.50%||Announcement date: Jan 29, 2020||Record date: Feb 18, 2020||Ex-Div: Feb 17, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">79.80</td>
                    <td align="right" width="130">81.70</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">2.38</td>
                    <td align="right" width="140">81.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/bearings/menonbearings/MB01" style="text-decoration:none;color:#333333">Menon Bearings</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE071D01033','BSE','523828');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Menon Bearings closes below 50-Day Moving Average of 58.04 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">50.60</td>
                    <td align="right" width="130">51.80</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">2.37</td>
                    <td align="right" width="140">51.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/schneiderelectricinfrastructure/SEI04" style="text-decoration:none;color:#333333">Schneider Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE839M01018','BSE','534139');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Schneider Infra closes above 30-Day,200-Day Moving Average today.</span></li><li><span>Only Buyers in Schneider Infra on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">89.70</td>
                    <td align="right" width="130">91.80</td>
                    <td align="right" width="140">2.10</td>
                    <td align="right" width="140">2.34</td>
                    <td align="right" width="140">91.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electricequipment/hondasielpowerproducts/HSP02" style="text-decoration:none;color:#333333">Honda Siel</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE634A01018','BSE','522064');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Honda Siel closes below 200-Day Moving Average of 1086.39 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,035.00</td>
                    <td align="right" width="130">1,059.25</td>
                    <td align="right" width="140">24.25</td>
                    <td align="right" width="140">2.34</td>
                    <td align="right" width="140">1,059.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/aminesplasticizers/AP07" style="text-decoration:none;color:#333333">Amines Plast</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE275D01022','BSE','506248');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Amines Plast closes above 50-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">32.20</td>
                    <td align="right" width="130">32.95</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">2.33</td>
                    <td align="right" width="140">32.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/sugar/mawanasugars/MS25" style="text-decoration:none;color:#333333">Mawana Sugars</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE636A01039','BSE','523371');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mawana Sugars closes above 30-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">34.40</td>
                    <td align="right" width="130">35.20</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">2.33</td>
                    <td align="right" width="140">35.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/ncc/NCC01" style="text-decoration:none;color:#333333">NCC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE868B01028','BSE','500294');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Buy NCC; target of Rs 98: Prabhudas Lilladher</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">36.50</td>
                    <td align="right" width="130">37.35</td>
                    <td align="right" width="140">0.85</td>
                    <td align="right" width="140">2.33</td>
                    <td align="right" width="140">37.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/eclerxservices/eS06" style="text-decoration:none;color:#333333">eClerx Services</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE738I01010','BSE','532927');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>eClerx Services closes above 150-Day Moving Average of 527.98 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">534.75</td>
                    <td align="right" width="130">547.00</td>
                    <td align="right" width="140">12.25</td>
                    <td align="right" width="140">2.29</td>
                    <td align="right" width="140">547.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/packaging/moldtektechnologies/MTT01" style="text-decoration:none;color:#333333">Mold Tek Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE835B01035','BSE','526263');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mold Tek Tech closes below 50-Day Moving Average of 48.85 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">44.00</td>
                    <td align="right" width="130">45.00</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">2.27</td>
                    <td align="right" width="140">45.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/zentechnologies/ZT01" style="text-decoration:none;color:#333333">Zen Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE251B01027','BSE','533339');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Zen Tech closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">53.45</td>
                    <td align="right" width="130">54.65</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">2.25</td>
                    <td align="right" width="140">54.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/makerslaboratories/ML" style="text-decoration:none;color:#333333">Makers Labs</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE987A01010','BSE','506919');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Makers Labs on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">37.90</td>
                    <td align="right" width="130">38.75</td>
                    <td align="right" width="140">0.85</td>
                    <td align="right" width="140">2.24</td>
                    <td align="right" width="140">38.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/thehitechgears/HTG" style="text-decoration:none;color:#333333">The Hi-Tech Gea</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE127B01011','BSE','522073');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>The Hi-Tech Gea Dividend||Interim Dividend 15.00%||Announcement date: Feb 07, 2020||Record date: Feb 22, 2020||Ex-Div: Feb 18, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">147.00</td>
                    <td align="right" width="130">150.30</td>
                    <td align="right" width="140">3.30</td>
                    <td align="right" width="140">2.24</td>
                    <td align="right" width="140">150.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/mothersonsumisystems/MSS01" style="text-decoration:none;color:#333333">Motherson Sumi</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE775A01035','BSE','517334');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Motherson Sumi Block Deal on BSE||Qty: 1,621,632||Deal Price: 104.10||Value (cr): 16.88||Time: 09:16am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">105.45</td>
                    <td align="right" width="130">107.80</td>
                    <td align="right" width="140">2.35</td>
                    <td align="right" width="140">2.23</td>
                    <td align="right" width="140">107.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/responsiveindustries/SH10" style="text-decoration:none;color:#333333">Responsive Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE688D01026','BSE','505509');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Responsive Ind closes below 30-Day Moving Average of 90.34 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">86.00</td>
                    <td align="right" width="130">87.90</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">2.21</td>
                    <td align="right" width="140">87.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilescompositemills/naharindustrialenterprises/NIE" style="text-decoration:none;color:#333333">Nahar Ent</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE289A01011','BSE','519136');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nahar Ent closes below 50-Day Moving Average of 26.01 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">22.65</td>
                    <td align="right" width="130">23.15</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">2.21</td>
                    <td align="right" width="140">23.15</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electrodesgraphite/heg/HEG" style="text-decoration:none;color:#333333">HEG</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE545A01016','BSE','509631');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>HEG Dividend||Interim Dividend 250.00%||Announcement date: Feb 06, 2020||Record date: Feb 19, 2020||Ex-Div: Feb 17, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">932.00</td>
                    <td align="right" width="130">952.45</td>
                    <td align="right" width="140">20.45</td>
                    <td align="right" width="140">2.19</td>
                    <td align="right" width="140">952.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/oberoirealty/OR" style="text-decoration:none;color:#333333">Oberoi Realty</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE093I01010','BSE','533273');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Oberoi Realty Block Deal on NSE||Qty: 400,000||Deal Price: 500.00||Value (cr): 20.00||Time: 09:20am</span></li><li><span>Oberoi Realty Block Deal on NSE||Qty: 400,000||Deal Price: 500.00||Value (cr): 20.00||Time: 09:20am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">511.70</td>
                    <td align="right" width="130">522.85</td>
                    <td align="right" width="140">11.15</td>
                    <td align="right" width="140">2.18</td>
                    <td align="right" width="140">522.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/tatamotorsltddvr/TATAM57000" style="text-decoration:none;color:#333333">TML-D</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('IN9155A01020','BSE','570001');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>TML-D closes below 200-Day Moving Average of 73.12 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">55.65</td>
                    <td align="right" width="130">56.85</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">2.16</td>
                    <td align="right" width="140">56.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractinghousing/eldecohous/EH01" style="text-decoration:none;color:#333333">Eldeco Housing</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE668G01013','BSE','523329');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Eldeco Housing closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,400.00</td>
                    <td align="right" width="130">1,430.00</td>
                    <td align="right" width="140">30.00</td>
                    <td align="right" width="140">2.14</td>
                    <td align="right" width="140">1,430.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/conartengineers/CE05" style="text-decoration:none;color:#333333">Conart Engineer</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE714D01012','BSE','522231');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Conart Engineers: Outcome of board meeting</span></a></li><li><a href="javascript:void(0)"><span>Conart Engineers' board meeting on November 6, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/conartengineers/notices/CE05" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Conart Engineer Dividend||Interim Dividend 10.00%||Announcement date: Nov 08, 2019||Record date: Nov 21, 2019||Ex-Div: Nov 20, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.45</td>
                    <td align="right" width="130">23.95</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">2.13</td>
                    <td align="right" width="140">23.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textileshosieryknitwear/rupacompany/RC14" style="text-decoration:none;color:#333333">Rupa and Comp</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE895B01021','BSE','533552');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rupa and Comp closes below 30-Day Moving Average of 219.25 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">183.65</td>
                    <td align="right" width="130">187.50</td>
                    <td align="right" width="140">3.85</td>
                    <td align="right" width="140">2.10</td>
                    <td align="right" width="140">187.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/oilindia/OI13" style="text-decoration:none;color:#333333">Oil India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE274J01014','BSE','533106');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Oil India Dividend||Interim Dividend 90.00%||Announcement date: Feb 10, 2020||Record date: Feb 24, 2020||Ex-Div: Feb 20, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">104.55</td>
                    <td align="right" width="130">106.75</td>
                    <td align="right" width="140">2.20</td>
                    <td align="right" width="140">2.10</td>
                    <td align="right" width="140">106.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electrodesgraphite/esabindia/EI06" style="text-decoration:none;color:#333333">Esab India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE284A01012','BSE','500133');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Esab India closes above 50-Day Moving Average of 1441.88 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,449.90</td>
                    <td align="right" width="130">1,480.00</td>
                    <td align="right" width="140">30.10</td>
                    <td align="right" width="140">2.08</td>
                    <td align="right" width="140">1,480.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/tyres/ptlenterprises/PTL06" style="text-decoration:none;color:#333333">PTL Enterprises</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE034D01031','BSE','509220');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PTL Enterprises closes above  its 30-Day,50-Day,200-Day Moving Average today.</span></li><li><span>PTL Enterprises Dividend||Interim Dividend 125.00%||Announcement date: Feb 24, 2020||Record date: Mar 05, 2020||Ex-Div: Mar 04, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">37.15</td>
                    <td align="right" width="130">37.90</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">2.02</td>
                    <td align="right" width="140">37.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/diversified/irisbusinessservices/IBS01" style="text-decoration:none;color:#333333">IRIS Business S</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE864K01010','BSE','540735');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>IRIS Business Services: Outcome of board meeting</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/irisbusinessservices/notices/IBS01" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in IRIS Business S on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">27.50</td>
                    <td align="right" width="130">28.05</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">28.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pesticidesagrochemicals/naclindustries/NA04" style="text-decoration:none;color:#333333">Nacl Industries</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE295D01020','BSE','524709');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Nacl Industries to raise fund of Rs 300 crore</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/naclindustries/notices/NA04" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nacl Industries closes above 50-Day Moving Average of 29.66 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.95</td>
                    <td align="right" width="130">30.55</td>
                    <td align="right" width="140">0.60</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">30.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engineering/salasartechnoengineering/STE02" style="text-decoration:none;color:#333333">Salasar Techno </a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE170V01019','BSE','540642');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/salasar-techno-share-price-gains-6order-win_13530021.html" title="Salasar Techno share price gains 6% on order win"><span>Salasar Techno share price gains 6% on order win</span></a><em>Feb 26, 02:21</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/salasartechnoengineering/news/STE02" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Salasar Techno  closes above 150-Day Moving Average of 116.38 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">110.05</td>
                    <td align="right" width="130">112.25</td>
                    <td align="right" width="140">2.20</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">112.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/glassglassproducts/saintgobainsekurit/SGS01" style="text-decoration:none;color:#333333">Saint-Gobain</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE068B01017','BSE','515043');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Saint-Gobain on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">47.45</td>
                    <td align="right" width="130">48.40</td>
                    <td align="right" width="140">0.95</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">48.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/dyespigments/vipulorganics/VD01" style="text-decoration:none;color:#333333">Vipul Organics</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE834D01018','BSE','530627');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Vipul Dyechem on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">138.25</td>
                    <td align="right" width="130">141.00</td>
                    <td align="right" width="140">2.75</td>
                    <td align="right" width="140">1.99</td>
                    <td align="right" width="140">141.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powertransmissionequipment/kecinternational/KEC04" style="text-decoration:none;color:#333333">KEC Intl</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE389H01022','BSE','532714');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KEC Intl closes above 30-Day Moving Average of 337.47 today.</span></li><li><span>KEC Intl closes above 30-Day Moving Average of 337.47 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">315.05</td>
                    <td align="right" width="130">321.30</td>
                    <td align="right" width="140">6.25</td>
                    <td align="right" width="140">1.98</td>
                    <td align="right" width="140">321.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plantationsteacoffee/harrisonsmalyalam/HM02" style="text-decoration:none;color:#333333">Harrisons Malay</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE544A01019','BSE','500467');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Harrisons Malay closes above 30-Day,50-Day Moving Average today.</span></li><li><span>Harrisons Malay closes above 200-Day Moving Average of 58.04 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">61.20</td>
                    <td align="right" width="130">62.40</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">1.96</td>
                    <td align="right" width="140">62.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/dilipbuildcon/DB04" style="text-decoration:none;color:#333333">Dilip Buildcon</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE917M01012','BSE','540047');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Dilip Buildcon has hit 52wk low of Rs 311.15 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">304.00</td>
                    <td align="right" width="130">309.95</td>
                    <td align="right" width="140">5.95</td>
                    <td align="right" width="140">1.96</td>
                    <td align="right" width="140">309.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/indiamartintermesh/II12" style="text-decoration:none;color:#333333">Indiamart Inter</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE933S01016','BSE','542726');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Indiamart Inter closes above 30-Day Moving Average of 2413.95 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,530.35</td>
                    <td align="right" width="130">2,579.75</td>
                    <td align="right" width="140">49.40</td>
                    <td align="right" width="140">1.95</td>
                    <td align="right" width="140">2,579.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electricequipment/vguardindustries/VI02" style="text-decoration:none;color:#333333">V-Guard Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE951I01027','BSE','532953');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>V-Guard Ind Dividend||Interim Dividend 90.00%||Announcement date: Feb 14, 2020||Record date: Feb 27, 2020||Ex-Div: Feb 27, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">202.05</td>
                    <td align="right" width="130">206.00</td>
                    <td align="right" width="140">3.95</td>
                    <td align="right" width="140">1.95</td>
                    <td align="right" width="140">206.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pesticidesagrochemicals/aimcopesticides/AP03" style="text-decoration:none;color:#333333">Aimco Pesticide</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE008B01013','BSE','524288');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Aimco Pesticides' board meeting on September 14, 2017</span></a></li><li><a href="javascript:void(0)"><span>Aimco Pesticide's board meeting held on August 23, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/aimcopesticides/notices/AP03" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Aimco Pesticide has hit 52wk low of Rs 71.10 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">73.00</td>
                    <td align="right" width="130">74.40</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">1.92</td>
                    <td align="right" width="140">74.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/accelyakalesolutions/KAL" style="text-decoration:none;color:#333333">Accelya Kale</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE793A01012','BSE','532268');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Accelya Kale closes below 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,039.45</td>
                    <td align="right" width="130">1,059.30</td>
                    <td align="right" width="140">19.85</td>
                    <td align="right" width="140">1.91</td>
                    <td align="right" width="140">1,059.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesprocessing/ganeshaecosphere/GP01" style="text-decoration:none;color:#333333">Ganesha Ecosph</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE845D01014','BSE','514167');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ganesha Ecosph closes above 30-Day Moving Average of 321.75 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">321.95</td>
                    <td align="right" width="130">328.10</td>
                    <td align="right" width="140">6.15</td>
                    <td align="right" width="140">1.91</td>
                    <td align="right" width="140">328.10</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesdenim/kgdenim/KGD" style="text-decoration:none;color:#333333">KG Denim</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE104A01012','BSE','500239');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KG Denim has hit 52wk low of Rs 18.15 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.00</td>
                    <td align="right" width="130">29.55</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">29.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/vakrangee/VS" style="text-decoration:none;color:#333333">Vakrangee</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE051B01021','BSE','511431');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in Vakrangee on NSE</span></li><li><span>Only Sellers in Vakrangee on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">37.00</td>
                    <td align="right" width="130">37.70</td>
                    <td align="right" width="140">0.70</td>
                    <td align="right" width="140">1.89</td>
                    <td align="right" width="140">37.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/abmknowledgeware/ABM" style="text-decoration:none;color:#333333">ABM Knowledg</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE850B01026','BSE','531161');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>ABM Knowledg Dividend||Interim Dividend 25.00%||Announcement date: Feb 10, 2020||Record date: Feb 27, 2020||Ex-Div: Feb 26, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">53.00</td>
                    <td align="right" width="130">54.00</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.89</td>
                    <td align="right" width="140">54.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/leatherproducts/superhouse/SL" style="text-decoration:none;color:#333333">Superhouse</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE712B01010','BSE','523283');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Superhouse's board meeting on December 14, 2017</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/superhouse/notices/SL" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Superhouse closes below 150-Day Moving Average of 84.05 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">80.00</td>
                    <td align="right" width="130">81.50</td>
                    <td align="right" width="140">1.50</td>
                    <td align="right" width="140">1.88</td>
                    <td align="right" width="140">81.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/compressors/elgiequipments/EE01" style="text-decoration:none;color:#333333">Elgi Equipments</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE285A01027','BSE','522074');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Elgi Equipments has hit 52wk low of Rs 204.70 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">196.35</td>
                    <td align="right" width="130">200.05</td>
                    <td align="right" width="140">3.70</td>
                    <td align="right" width="140">1.88</td>
                    <td align="right" width="140">200.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electrodesgraphite/panasoniccarbonindia/PCI04" style="text-decoration:none;color:#333333">PanasonicCarbon</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE013E01017','BSE','508941');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PanasonicCarbon closes above 30-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">375.00</td>
                    <td align="right" width="130">382.00</td>
                    <td align="right" width="140">7.00</td>
                    <td align="right" width="140">1.87</td>
                    <td align="right" width="140">382.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/auto23wheelers/endurancetechnologies/ET01" style="text-decoration:none;color:#333333">Endurance Techn</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE913H01037','BSE','540153');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Endurance Techn closes below 200-Day Moving Average of 1045.48 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">968.45</td>
                    <td align="right" width="130">986.40</td>
                    <td align="right" width="140">17.95</td>
                    <td align="right" width="140">1.85</td>
                    <td align="right" width="140">986.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engineeringheavy/gardenreachshipbuildersengineers/GRS01" style="text-decoration:none;color:#333333">Garden Reach Sh</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE382Z01011','BSE','542011');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Garden Reach Sh closes above 150-Day Moving Average of 178.34 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">162.30</td>
                    <td align="right" width="130">165.30</td>
                    <td align="right" width="140">3.00</td>
                    <td align="right" width="140">1.85</td>
                    <td align="right" width="140">165.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/diamondcuttingjewellerypreciousmetals/tribhovandasbhimjizaveri/TBZ" style="text-decoration:none;color:#333333">Tribhovandas</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE760L01018','BSE','534369');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Tribhovandas closes above 150-Day Moving Average of 39.24 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.95</td>
                    <td align="right" width="130">30.50</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">1.84</td>
                    <td align="right" width="140">30.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/pricol/P9" style="text-decoration:none;color:#333333">Pricol</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE726V01018','BSE','540293');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Pricol on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">35.45</td>
                    <td align="right" width="130">36.10</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">1.83</td>
                    <td align="right" width="140">36.10</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/royalorchidhotels/RO01" style="text-decoration:none;color:#333333">Royal Orchid</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE283H01019','BSE','532699');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Royal Orchid closes above 200-Day Moving Average of 84.39 today.</span></li><li><span>Only Buyers in Royal Orchid on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">57.70</td>
                    <td align="right" width="130">58.75</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">1.82</td>
                    <td align="right" width="140">58.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/powergridcorporationindia/PGC" style="text-decoration:none;color:#333333">Power Grid Corp</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE752E01010','BSE','532898');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/stocksthe-news-power-grid-pidilite-industries-jubilant-food-rites-bankbaroda_13535681.html" title="Stocks in the news: Power Grid, Pidilite Industries, Jubilant Food, RITES, Bank of Baroda"><span>Stocks in the news: Power Grid, Pidilite Industries, Jubilant Food, RITES, Bank of Baroda</span></a><em>Feb 28, 07:50</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/powergridcorporationindia/news/PGC" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Power Grid Corp closes above 30-Day,50-Day Moving Average today.</span></li><li><span>Power Grid Corp Block Deal on NSE||Qty: 833,134||Deal Price: 182.25||Value (cr): 15.18||Time: 09:39am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">188.05</td>
                    <td align="right" width="130">191.45</td>
                    <td align="right" width="140">3.40</td>
                    <td align="right" width="140">1.81</td>
                    <td align="right" width="140">191.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powertransmissionequipment/voltamptransformers/VT9" style="text-decoration:none;color:#333333">Voltamp Trans</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE540H01012','BSE','532757');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Buy Voltamp Transformers; target of Rs 1591: Prabhudas Lilladher</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,257.75</td>
                    <td align="right" width="130">1,280.50</td>
                    <td align="right" width="140">22.75</td>
                    <td align="right" width="140">1.81</td>
                    <td align="right" width="140">1,280.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/nmdc/NMD02" style="text-decoration:none;color:#333333">NMDC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE584A01023','BSE','526371');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>NMDC Dividend||Interim Dividend 529.00%||Announcement date: Feb 06, 2020||Record date: Feb 21, 2020||Ex-Div: Feb 18, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">91.85</td>
                    <td align="right" width="130">93.50</td>
                    <td align="right" width="140">1.65</td>
                    <td align="right" width="140">1.80</td>
                    <td align="right" width="140">93.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/oilnaturalgascorporation/ONG" style="text-decoration:none;color:#333333">ONGC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE213A01029','BSE','500312');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/ongc-hpcl-buy-out-bankerspetronet-mhb-for-rs-371cr_13535621.html" title="ONGC, HPCL buy out bankers in Petronet MHB for Rs 371cr"><span>ONGC, HPCL buy out bankers in Petronet MHB for Rs 371cr</span></a><em>Feb 27, 10:45</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/oilnaturalgascorporation/news/ONG" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">91.65</td>
                    <td align="right" width="130">93.30</td>
                    <td align="right" width="140">1.65</td>
                    <td align="right" width="140">1.80</td>
                    <td align="right" width="140">93.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/consumergoodselectronic/orientelectriclimited/ORIEN54130" style="text-decoration:none;color:#333333">Orient Electric</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE142Z01019','BSE','541301');"></span><div class="MT5"></div></td>
                    <td align="right" width="130">257.75</td>
                    <td align="right" width="130">262.40</td>
                    <td align="right" width="140">4.65</td>
                    <td align="right" width="140">1.80</td>
                    <td align="right" width="140">262.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engineering/ionexchangeindia/IEI" style="text-decoration:none;color:#333333">Ion Exchange</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE570A01014','BSE','500214');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ion Exchange closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">865.00</td>
                    <td align="right" width="130">880.45</td>
                    <td align="right" width="140">15.45</td>
                    <td align="right" width="140">1.79</td>
                    <td align="right" width="140">880.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/aurolaboratories/AL06" style="text-decoration:none;color:#333333">Auro Labs</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE292C01011','BSE','530233');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Auro Labs has hit 52wk low of Rs 36.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">36.30</td>
                    <td align="right" width="130">36.95</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">1.79</td>
                    <td align="right" width="140">36.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/fertiliserschemicalstravancore/FCT" style="text-decoration:none;color:#333333">Fert and Chem</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE188A01015','BSE','590024');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Fert and Chem closes below 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">30.90</td>
                    <td align="right" width="130">31.45</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">1.78</td>
                    <td align="right" width="140">31.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/sjvn/S11" style="text-decoration:none;color:#333333">SJVN</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE002L01015','BSE','533206');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>SJVN Dividend||Interim Dividend 17.00%||Announcement date: Feb 13, 2020||Record date: Feb 26, 2020||Ex-Div: Feb 25, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.00</td>
                    <td align="right" width="130">23.40</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.74</td>
                    <td align="right" width="140">23.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/castingsforgings/mahindracieautomotive/MF19" style="text-decoration:none;color:#333333">Mahindra CIE</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE536H01010','BSE','532756');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mahindra CIE has hit 52wk low of Rs 132.55 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">126.45</td>
                    <td align="right" width="130">128.65</td>
                    <td align="right" width="140">2.20</td>
                    <td align="right" width="140">1.74</td>
                    <td align="right" width="140">128.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/packaging/timetechnoplast/TT03" style="text-decoration:none;color:#333333">Time Techno</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE508G01029','BSE','532856');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Time Techno closes below 50-Day Moving Average of 53.88 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">46.20</td>
                    <td align="right" width="130">47.00</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.73</td>
                    <td align="right" width="140">47.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/xelpmocdesigntech/XDT" style="text-decoration:none;color:#333333">Xelpmoc Design </a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE01P501012','BSE','542367');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Xelpmoc Design  POM on Feb 21, 2020||Announcement date: Jan 20, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">51.95</td>
                    <td align="right" width="130">52.85</td>
                    <td align="right" width="140">0.90</td>
                    <td align="right" width="140">1.73</td>
                    <td align="right" width="140">52.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/godrejagrovet/GA03" style="text-decoration:none;color:#333333">Godrej Agrovet</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE850D01014','BSE','540743');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Godrej Agrovet Block Deal on BSE||Qty: 314,011||Deal Price: 539.00||Value (cr): 16.93||Time: 09:22am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">460.50</td>
                    <td align="right" width="130">468.40</td>
                    <td align="right" width="140">7.90</td>
                    <td align="right" width="140">1.72</td>
                    <td align="right" width="140">468.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/rajratanglobalwire/RGW01" style="text-decoration:none;color:#333333">Rajratan Global</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE451D01011','BSE','517522');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rajratan Global closes above 50-Day Moving Average of 343.98 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">293.00</td>
                    <td align="right" width="130">298.00</td>
                    <td align="right" width="140">5.00</td>
                    <td align="right" width="140">1.71</td>
                    <td align="right" width="140">298.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textileshosieryknitwear/naharspinningmills/NSM" style="text-decoration:none;color:#333333">Nahar Spinning</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE290A01027','BSE','500296');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nahar Spinning has hit 52wk low of Rs 38.30 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">35.15</td>
                    <td align="right" width="130">35.75</td>
                    <td align="right" width="140">0.60</td>
                    <td align="right" width="140">1.71</td>
                    <td align="right" width="140">35.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/lasasupergenerics/LS06" style="text-decoration:none;color:#333333">Lasa Supergener</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE670X01014','BSE','540702');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/lasa-supergenerics-acquires-harishree-aromatics-share-price-lockedupper-circuit_13533661.html" title="Lasa Supergenerics acquires Harishree Aromatics, share price locked in upper circuit"><span>Lasa Supergenerics acquires Harishree Aromatics, share price locked in upper circuit</span></a><em>Feb 27, 02:38</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/lasasupergenerics/news/LS06" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Lasa Supergener on NSE</span></li><li><span>Only Buyers in Lasa Supergener on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">47.00</td>
                    <td align="right" width="130">47.80</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.70</td>
                    <td align="right" width="140">47.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/paper/southindiapapermills/SIP03" style="text-decoration:none;color:#333333">South (I) Paper</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE088G01014','BSE','516108');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in South (I) Paper on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">59.00</td>
                    <td align="right" width="130">60.00</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.69</td>
                    <td align="right" width="140">60.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/hexawaretechnologies/HT02" style="text-decoration:none;color:#333333">Hexaware Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE093A01033','BSE','532129');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Hexaware Tech closes above 30-Day Moving Average of 363.92 today.</span></li><li><span>Hexaware Tech closes below 30-Day Moving Average of 362.47 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">360.70</td>
                    <td align="right" width="130">366.80</td>
                    <td align="right" width="140">6.10</td>
                    <td align="right" width="140">1.69</td>
                    <td align="right" width="140">366.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/paper/satiaindustries/SI96" style="text-decoration:none;color:#333333">Satia Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE170E01015','BSE','539201');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Satia Ind Dividend||Interim Dividend 15.00%||Announcement date: Jan 30, 2020||Record date: Feb 22, 2020||Ex-Div: Feb 18, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">95.50</td>
                    <td align="right" width="130">97.10</td>
                    <td align="right" width="140">1.60</td>
                    <td align="right" width="140">1.68</td>
                    <td align="right" width="140">97.10</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/safariindustriesindia/SII01" style="text-decoration:none;color:#333333">Safari Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE429E01023','BSE','523025');"></span><div class="MT5"></div></td>
                    <td align="right" width="130">575.00</td>
                    <td align="right" width="130">584.60</td>
                    <td align="right" width="140">9.60</td>
                    <td align="right" width="140">1.67</td>
                    <td align="right" width="140">584.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/foodprocessing/sheetalcoolproducts/SCP" style="text-decoration:none;color:#333333">Sheetal Cool Pr</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE501Y01019','BSE','540757');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sheetal Cool Pr closes above 150-Day Moving Average of 117.19 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">131.70</td>
                    <td align="right" width="130">133.90</td>
                    <td align="right" width="140">2.20</td>
                    <td align="right" width="140">1.67</td>
                    <td align="right" width="140">133.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingrealestate/anantraj/ARI" style="text-decoration:none;color:#333333">Anant Raj</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE242C01024','BSE','515055');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Anant Raj closes below 200-Day Moving Average of 31.72 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">27.15</td>
                    <td align="right" width="130">27.60</td>
                    <td align="right" width="140">0.45</td>
                    <td align="right" width="140">1.66</td>
                    <td align="right" width="140">27.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/venkys/V03" style="text-decoration:none;color:#333333">Venkys</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE398A01010','BSE','523261');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Venkys closes below 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,203.00</td>
                    <td align="right" width="130">1,223.00</td>
                    <td align="right" width="140">20.00</td>
                    <td align="right" width="140">1.66</td>
                    <td align="right" width="140">1,223.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/pnbgilts/PNB04" style="text-decoration:none;color:#333333">PNB Gilts</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE859A01011','BSE','532366');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>PNB Gilts closes above 150-Day Moving Average of 30.20 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">30.05</td>
                    <td align="right" width="130">30.55</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">1.66</td>
                    <td align="right" width="140">30.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesspinningcottonblended/nitinspinners/NS12" style="text-decoration:none;color:#333333">Nitin Spinners</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE229H01012','BSE','532698');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nitin Spinners closes above 30-Day Moving Average of 55.37 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">45.50</td>
                    <td align="right" width="130">46.25</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">1.65</td>
                    <td align="right" width="140">46.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engineeringheavy/gmmpfaudler/GMM01" style="text-decoration:none;color:#333333">GMM Pfaudler</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE541A01023','BSE','505255');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>GMM Pfaudler closes above 30-Day Moving Average of 2904.84 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,996.20</td>
                    <td align="right" width="130">3,045.45</td>
                    <td align="right" width="140">49.25</td>
                    <td align="right" width="140">1.64</td>
                    <td align="right" width="140">3,045.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/sugar/triveniengineeringindustries/TE10" style="text-decoration:none;color:#333333">Triveni Engg</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE256C01024','BSE','532356');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Triveni Engg Dividend||Interim Dividend 110.00%||Announcement date: Feb 10, 2020||Record date: Feb 20, 2020||Ex-Div: Feb 18, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">61.05</td>
                    <td align="right" width="130">62.05</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.64</td>
                    <td align="right" width="140">62.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pumps/ksb/KSB" style="text-decoration:none;color:#333333">KSB Pumps</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE999A01015','BSE','500249');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>KSB Pumps closes above 200-Day Moving Average of 672.35 today.</span></li><li><span>KSB Pumps closes below 200-Day Moving Average of 672.15 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">674.70</td>
                    <td align="right" width="130">685.65</td>
                    <td align="right" width="140">10.95</td>
                    <td align="right" width="140">1.62</td>
                    <td align="right" width="140">685.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/jindalsaw/JS08" style="text-decoration:none;color:#333333">Jindal Saw</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE324A01024','BSE','500378');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Jindal Saw closes above 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">80.40</td>
                    <td align="right" width="130">81.70</td>
                    <td align="right" width="140">1.30</td>
                    <td align="right" width="140">1.62</td>
                    <td align="right" width="140">81.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/shilpamedicare/SM19" style="text-decoration:none;color:#333333">Shilpa</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE790G01031','BSE','530549');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/shilpa-medicare-share-price-locked-at-lower-circuit15-observationsusfda_13529721.html" title="Shilpa Medicare share price locked at lower circuit on 15 observations from USFDA"><span>Shilpa Medicare share price locked at lower circuit on 15 observations from USFDA</span></a><em>Feb 26, 01:15</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/shilpamedicare/news/SM19" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Buyers in Shilpa on BSE</span></li><li><span>Only Sellers in Shilpa on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">429.95</td>
                    <td align="right" width="130">436.85</td>
                    <td align="right" width="140">6.90</td>
                    <td align="right" width="140">1.60</td>
                    <td align="right" width="140">436.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/thirumalaichemicals/TC07" style="text-decoration:none;color:#333333">Thirumalai Chem</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE338A01024','BSE','500412');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Thirumalai Chem closes above 200-Day Moving Average of 73.27 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">62.95</td>
                    <td align="right" width="130">63.95</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.59</td>
                    <td align="right" width="140">63.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cigarettes/vstindustries/VST" style="text-decoration:none;color:#333333">VST</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE710A01016','BSE','509966');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>VST closes below 50-Day Moving Average of 4333.32 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">4,125.20</td>
                    <td align="right" width="130">4,190.00</td>
                    <td align="right" width="140">64.80</td>
                    <td align="right" width="140">1.57</td>
                    <td align="right" width="140">4,190.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/zensartechnologies/ZT02" style="text-decoration:none;color:#333333">Zensar Tech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE520A01027','BSE','504067');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Zensar Tech Dividend||Interest Dividend 50.00%||Announcement date: Jan 23, 2020||Record date: Feb 07, 2020||Ex-Div: Feb 06, 2020</span></li><li><span>Zensar Tech Dividend||Interim Dividend 50.00%||Announcement date: Jan 23, 2020||Record date: Feb 07, 2020||Ex-Div: Feb 06, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">134.90</td>
                    <td align="right" width="130">137.00</td>
                    <td align="right" width="140">2.10</td>
                    <td align="right" width="140">1.56</td>
                    <td align="right" width="140">137.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/gatewaydistriparks/GD01" style="text-decoration:none;color:#333333">Gateway Distri</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE852F01015','BSE','532622');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Gateway Distri closes below 30-Day Moving Average of 129.61 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">122.00</td>
                    <td align="right" width="130">123.90</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">1.56</td>
                    <td align="right" width="140">123.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/jagsonpalpharmaceuticals/JP02" style="text-decoration:none;color:#333333">JagsonpalPharma</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE048B01027','BSE','507789');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>JagsonpalPharma closes above 30-Day Moving Average of 27.33 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">25.80</td>
                    <td align="right" width="130">26.20</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.55</td>
                    <td align="right" width="140">26.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/indoboraxchemicals/IBC" style="text-decoration:none;color:#333333">Indo Borax</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE803D01013','BSE','524342');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Indo Borax: Outcome of board meeting</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/indoboraxchemicals/notices/IBC" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Indo Borax has hit 52wk low of Rs 316.25 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">320.00</td>
                    <td align="right" width="130">324.90</td>
                    <td align="right" width="140">4.90</td>
                    <td align="right" width="140">1.53</td>
                    <td align="right" width="140">324.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/ashapuraminechem/AM07" style="text-decoration:none;color:#333333">Ashapura Mine</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE348A01023','BSE','527001');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ashapura Mine closes above 50-Day Moving Average of 33.47 today.</span></li><li><span>Only Sellers in Ashapura Mine on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">33.00</td>
                    <td align="right" width="130">33.50</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">1.52</td>
                    <td align="right" width="140">33.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cementproductsbuildingmaterials/morganitecrucibleindia/MCI05" style="text-decoration:none;color:#333333">Morganite India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE599F01012','BSE','523160');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Morganite India POM on Nov 30, 2019||Announcement date: Oct 18, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,970.00</td>
                    <td align="right" width="130">2,000.00</td>
                    <td align="right" width="140">30.00</td>
                    <td align="right" width="140">1.52</td>
                    <td align="right" width="140">2,000.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/iciciprudentialnv20etf/ICI13" style="text-decoration:none;color:#333333">IPRU NV20 ETF</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INF109KB1WY5','BSE','539945');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>IPRU NV20 ETF closes below 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">53.80</td>
                    <td align="right" width="130">54.62</td>
                    <td align="right" width="140">0.82</td>
                    <td align="right" width="140">1.52</td>
                    <td align="right" width="140">54.62</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/teamleaseservices/TS13" style="text-decoration:none;color:#333333">TeamLease Ser.</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE985S01024','BSE','539658');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>TeamLease Ser. Block Deal on NSE||Qty: 59,000||Deal Price: 2,495.00||Value (cr): 14.72||Time: 09:45am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,363.05</td>
                    <td align="right" width="130">2,399.00</td>
                    <td align="right" width="140">35.95</td>
                    <td align="right" width="140">1.52</td>
                    <td align="right" width="140">2,399.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engines/kirloskaroilengines/KOE03" style="text-decoration:none;color:#333333">Kirloskar Oil</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE146L01010','BSE','533293');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kirloskar Oil has hit 52wk low of Rs 134.20 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">125.75</td>
                    <td align="right" width="130">127.65</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">1.51</td>
                    <td align="right" width="140">127.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftware/ramcosystem/RS17" style="text-decoration:none;color:#333333">Ramco System</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE246B01019','BSE','532370');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ramco System closes below 50-Day Moving Average of 166.90 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">129.50</td>
                    <td align="right" width="130">131.45</td>
                    <td align="right" width="140">1.95</td>
                    <td align="right" width="140">1.51</td>
                    <td align="right" width="140">131.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/paper/kuantumpapers/ABC07" style="text-decoration:none;color:#333333">Kuantum Papers</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE529I01013','BSE','532937');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kuantum Papers closes above 150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">456.25</td>
                    <td align="right" width="130">463.15</td>
                    <td align="right" width="140">6.90</td>
                    <td align="right" width="140">1.51</td>
                    <td align="right" width="140">463.15</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/granulesindia/GI25" style="text-decoration:none;color:#333333">Granules India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE101D01020','BSE','532482');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/market-outlook/39breach11000-mark-is-quite-likely-granules-dabur-among-top-buys39_13542461.html" title="'Breach of 11,000-mark is quite likely; Granules, Dabur among top buys'"><span>'Breach of 11,000-mark is quite likely; Granules, Dabur among top buys'</span></a><em>Mar 02, 02:09</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/granulesindia/news/GI25" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Granules India closes above 30-Day Moving Average of 161.93 today.</span></li><li><span>Granules India closes above 30-Day Moving Average of 161.08 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">162.70</td>
                    <td align="right" width="130">165.15</td>
                    <td align="right" width="140">2.45</td>
                    <td align="right" width="140">1.51</td>
                    <td align="right" width="140">165.15</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/abanoffshore/AO04" style="text-decoration:none;color:#333333">Aban Offshore</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE421A01028','BSE','523204');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Aban Offshore has hit 52wk low of Rs 20.10 on BSE</span></li><li><span>Aban Offshore has hit 52wk low of Rs 20.10 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">19.95</td>
                    <td align="right" width="130">20.25</td>
                    <td align="right" width="140">0.30</td>
                    <td align="right" width="140">1.50</td>
                    <td align="right" width="140">20.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/couriers/gati/G04" style="text-decoration:none;color:#333333">Gati</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE152B01027','BSE','532345');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Gati closes below 30-Day Moving Average of 67.47 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">66.50</td>
                    <td align="right" width="130">67.50</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.50</td>
                    <td align="right" width="140">67.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steelrolling/manaksia/M16" style="text-decoration:none;color:#333333">Manaksia</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE015D01022','BSE','532932');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Manaksia closes above 30-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">50.60</td>
                    <td align="right" width="130">51.35</td>
                    <td align="right" width="140">0.75</td>
                    <td align="right" width="140">1.48</td>
                    <td align="right" width="140">51.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/ariesagro/AA02" style="text-decoration:none;color:#333333">Aries Agro</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE298I01015','BSE','532935');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Aries Agro closes above 150-Day Moving Average of 62.08 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">54.00</td>
                    <td align="right" width="130">54.80</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.48</td>
                    <td align="right" width="140">54.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/telecommunicationsservice/onmobileglobal/OG01" style="text-decoration:none;color:#333333">OnMobile Global</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE809I01019','BSE','532944');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>OnMobile Global closes below 30-Day Moving Average of 31.50 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.65</td>
                    <td align="right" width="130">24.00</td>
                    <td align="right" width="140">0.35</td>
                    <td align="right" width="140">1.48</td>
                    <td align="right" width="140">24.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/coalindia/CI11" style="text-decoration:none;color:#333333">Coal India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE522F01014','BSE','533278');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/coal-india-share-price-jumps-4better-production-numbers_13541601.html" title="Coal India share price jumps 4% on better production numbers"><span>Coal India share price jumps 4% on better production numbers</span></a><em>Mar 02, 11:30</em></span></li><li><span><a href="https://www.moneycontrol.com/news/business/coal-india-february-production-likely-to-be-66-million-tonnes_13539941.html" title="Coal India February production likely to be 66 million tonnes"><span>Coal India February production likely to be 66 million tonnes</span></a><em>Feb 29, 08:57</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/coalindia/news/CI11" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Coal India Block Deal on NSE||Qty: 518,899||Deal Price: 172.80||Value (cr): 8.97||Time: 09:52am</span></li><li><span>Coal India Block Deal on NSE||Qty: 512,207||Deal Price: 173.10||Value (cr): 8.87||Time: 09:58am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">175.50</td>
                    <td align="right" width="130">178.10</td>
                    <td align="right" width="140">2.60</td>
                    <td align="right" width="140">1.48</td>
                    <td align="right" width="140">178.10</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesprocessing/aymsyntex/WS01" style="text-decoration:none;color:#333333">AYM Syntex</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE193B01039','BSE','508933');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>AYM Syntex closes above  its 30-Day,50-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">30.60</td>
                    <td align="right" width="130">31.05</td>
                    <td align="right" width="140">0.45</td>
                    <td align="right" width="140">1.47</td>
                    <td align="right" width="140">31.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/glenmarkpharma/GP08" style="text-decoration:none;color:#333333">Glenmark</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE935A01035','BSE','532296');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/glenmark-inks-licensing-pacthikma-for-commercialisationnasal-spray-ryaltrisus_13533741.html" title="Glenmark inks licensing pact with Hikma for commercialisation of nasal spray Ryaltris in US"><span>Glenmark inks licensing pact with Hikma for commercialisation of nasal spray Ryaltris in US</span></a><em>Feb 27, 03:15</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/glenmarkpharma/news/GP08" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">278.50</td>
                    <td align="right" width="130">282.60</td>
                    <td align="right" width="140">4.10</td>
                    <td align="right" width="140">1.47</td>
                    <td align="right" width="140">282.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/petrochemicals/nocil/NOC02" style="text-decoration:none;color:#333333">NOCIL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE163A01018','BSE','500730');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>NOCIL closes above  its 50-Day,150-Day,200-Day Moving Average today.</span></li><li><span>NOCIL: New capacity, demand recovery and exports point to a revival in FY21</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">92.50</td>
                    <td align="right" width="130">93.85</td>
                    <td align="right" width="140">1.35</td>
                    <td align="right" width="140">1.46</td>
                    <td align="right" width="140">93.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/edibleoilssolventextraction/agrotechfoods/ATF" style="text-decoration:none;color:#333333">Agro Tech Foods</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE209A01019','BSE','500215');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Agro Tech Foods closes below 30-Day Moving Average of 698.16 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">618.00</td>
                    <td align="right" width="130">627.00</td>
                    <td align="right" width="140">9.00</td>
                    <td align="right" width="140">1.46</td>
                    <td align="right" width="140">627.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/retail/futureretail/FR" style="text-decoration:none;color:#333333">Future Retail</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE752P01024','BSE','540064');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Future Retail has hit 52wk low of Rs 308.30 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">301.90</td>
                    <td align="right" width="130">306.30</td>
                    <td align="right" width="140">4.40</td>
                    <td align="right" width="140">1.46</td>
                    <td align="right" width="140">306.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pesticidesagrochemicals/rallisindia/RI03" style="text-decoration:none;color:#333333">Rallis India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE613A01020','BSE','500355');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Rallis India closes above 50-Day Moving Average of 213.32 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">221.15</td>
                    <td align="right" width="130">224.35</td>
                    <td align="right" width="140">3.20</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">224.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/couriers/bluedartexpress/BDE" style="text-decoration:none;color:#333333">Blue Dart</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE233B01017','BSE','526612');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Blue Dart closes above 30-Day Moving Average of 2806.34 today.</span></li><li><span>Blue Dart closes below 30-Day Moving Average of 2789.82 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,920.00</td>
                    <td align="right" width="130">2,962.35</td>
                    <td align="right" width="140">42.35</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">2,962.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/nirlon/N02" style="text-decoration:none;color:#333333">Nirlon</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE910A01012','BSE','500307');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nirlon closes above 30-Day Moving Average of 264.28 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">275.00</td>
                    <td align="right" width="130">279.00</td>
                    <td align="right" width="140">4.00</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">279.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/jswenergy/JE01" style="text-decoration:none;color:#333333">JSW Energy</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE121E01018','BSE','533148');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>JSW Energy closes above 30-Day Moving Average of 65.41 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">56.40</td>
                    <td align="right" width="130">57.20</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.42</td>
                    <td align="right" width="140">57.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/gujaratgas/GGC" style="text-decoration:none;color:#333333">Gujarat Gas</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE844O01030','BSE','539336');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Gujarat Gas closes below 30-Day Moving Average of 289.34 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">285.40</td>
                    <td align="right" width="130">289.45</td>
                    <td align="right" width="140">4.05</td>
                    <td align="right" width="140">1.42</td>
                    <td align="right" width="140">289.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/kilitchdrugsindia/KDI" style="text-decoration:none;color:#333333">Kilitch Drugs</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE729D01010','BSE','524500');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kilitch Drugs closes below 150-Day Moving Average of 119.66 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">102.40</td>
                    <td align="right" width="130">103.85</td>
                    <td align="right" width="140">1.45</td>
                    <td align="right" width="140">1.42</td>
                    <td align="right" width="140">103.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/alembicpharmaceuticals/AP35" style="text-decoration:none;color:#333333">Alembic Pharma</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE901L01018','BSE','533573');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Alembic Pharma closes above 30-Day Moving Average of 634.36 today.</span></li><li><span>Alembic Pharma closes below 30-Day Moving Average of 632.43 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">650.10</td>
                    <td align="right" width="130">659.25</td>
                    <td align="right" width="140">9.15</td>
                    <td align="right" width="140">1.41</td>
                    <td align="right" width="140">659.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/sandurmanganeseironores/SMI" style="text-decoration:none;color:#333333">Sandur Manganes</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE149K01016','BSE','504918');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sandur Manganes has hit 52wk low of Rs 562.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">645.00</td>
                    <td align="right" width="130">654.00</td>
                    <td align="right" width="140">9.00</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">654.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/foodprocessing/flexfoods/FF03" style="text-decoration:none;color:#333333">Flex Foods</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE954B01018','BSE','523672');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Flex Foods has hit 52wk low of Rs 37.00 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">36.20</td>
                    <td align="right" width="130">36.70</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">1.38</td>
                    <td align="right" width="140">36.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/tyres/balkrishnaindustries/BI03" style="text-decoration:none;color:#333333">Balkrishna Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE787D01026','BSE','502355');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Balkrishna Ind closes above 50-Day Moving Average of 1090.19 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,105.20</td>
                    <td align="right" width="130">1,120.45</td>
                    <td align="right" width="140">15.25</td>
                    <td align="right" width="140">1.38</td>
                    <td align="right" width="140">1,120.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/retail/adityabirlafashionretail/PFR" style="text-decoration:none;color:#333333">Aditya Birla F</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE647O01011','BSE','535755');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Aditya Birla F closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">251.00</td>
                    <td align="right" width="130">254.45</td>
                    <td align="right" width="140">3.45</td>
                    <td align="right" width="140">1.37</td>
                    <td align="right" width="140">254.45</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/shardamotorindustries/SMI04" style="text-decoration:none;color:#333333">Sharda Motor</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE597I01010','BSE','535602');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sharda Motor closes below  its 30-Day,50-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">809.00</td>
                    <td align="right" width="130">820.00</td>
                    <td align="right" width="140">11.00</td>
                    <td align="right" width="140">1.36</td>
                    <td align="right" width="140">820.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/machinetools/itlindustries/ITL" style="text-decoration:none;color:#333333">ITL Industries</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE478D01014','BSE','522183');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>ITL Industries has hit 52wk low of Rs 68.05 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">59.00</td>
                    <td align="right" width="130">59.80</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.36</td>
                    <td align="right" width="140">59.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/trading/singerindia/SI26" style="text-decoration:none;color:#333333">Singer India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE638A01035','BSE','505729');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Singer India has hit 52wk low of Rs 25.60 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">25.85</td>
                    <td align="right" width="130">26.20</td>
                    <td align="right" width="140">0.35</td>
                    <td align="right" width="140">1.35</td>
                    <td align="right" width="140">26.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/relianceetfnifty100/RSC03" style="text-decoration:none;color:#333333">R ETF Nifty 100</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INF204K014N5','BSE','537483');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>R ETF Nifty 100 closes above 150-Day Moving Average of 118.74 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">116.63</td>
                    <td align="right" width="130">118.21</td>
                    <td align="right" width="140">1.58</td>
                    <td align="right" width="140">1.35</td>
                    <td align="right" width="140">118.21</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/igpetrochemicals/IGP" style="text-decoration:none;color:#333333">IG Petro</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE204A01010','BSE','500199');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>IG Petro closes above 50-Day Moving Average of 168.69 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">156.90</td>
                    <td align="right" width="130">159.00</td>
                    <td align="right" width="140">2.10</td>
                    <td align="right" width="140">1.34</td>
                    <td align="right" width="140">159.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/plastics/mahindraepcirrigation/EPC" style="text-decoration:none;color:#333333">Mahindra EPC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE215D01010','BSE','523754');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mahindra EPC has hit 52wk low of Rs 76.05 on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">116.75</td>
                    <td align="right" width="130">118.30</td>
                    <td align="right" width="140">1.55</td>
                    <td align="right" width="140">1.33</td>
                    <td align="right" width="140">118.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/tycheindustries/TI30" style="text-decoration:none;color:#333333">Tyche Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE443B01012','BSE','532384');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Tyche Industries: Strong Q2 points to step-up in utilisation levels</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">106.40</td>
                    <td align="right" width="130">107.80</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">1.32</td>
                    <td align="right" width="140">107.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/financeinvestments/dolatinvestments/DI11" style="text-decoration:none;color:#333333">Dolat Investmen</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE966A01022','BSE','505526');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Dolat Investmen closes below 150-Day Moving Average of 55.88 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">49.40</td>
                    <td align="right" width="130">50.05</td>
                    <td align="right" width="140">0.65</td>
                    <td align="right" width="140">1.32</td>
                    <td align="right" width="140">50.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/tatachemicals/TC" style="text-decoration:none;color:#333333">Tata Chemicals</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE092A01019','BSE','500770');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/buzzing-stocks/radhakishan-gopikishan-damani-buy-more-india-cements-shares-raise-stake-to-116_13531081.html" title="Radhakishan, Gopikishan Damani buy more India Cements shares; raise stake to 11.6%"><span>Radhakishan, Gopikishan Damani buy more India Cements shares; raise stake to 11.6%</span></a><em>Feb 26, 08:07</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/tatachemicals/news/TC" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Tata Chemicals closes below 50-Day Moving Average of 724.37 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">720.20</td>
                    <td align="right" width="130">729.70</td>
                    <td align="right" width="140">9.50</td>
                    <td align="right" width="140">1.32</td>
                    <td align="right" width="140">729.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autolcvshcvs/eichermotors/EM" style="text-decoration:none;color:#333333">Eicher Motors</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE066A01013','BSE','505200');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/eicher-motors-bs-4-inventory-bare-minimum-ready-for-bs-6-transition_13548561.html" title="Eicher Motors: BS 4 inventory bare minimum; ready for BS 6 transition"><span>Eicher Motors: BS 4 inventory bare minimum; ready for BS 6 transition</span></a><em>Mar 03, 09:26</em></span></li><li><span><a href="https://www.moneycontrol.com/news/business/ve-commercial-vehicles-unveils-bs-vi-range-deliveries-begin-march_13545941.html" title="VE Commercial Vehicles unveils BS-VI range, deliveries begin March"><span>VE Commercial Vehicles unveils BS-VI range, deliveries begin March</span></a><em>Mar 03, 12:35</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/eichermotors/news/EM" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">17,745.05</td>
                    <td align="right" width="130">17,978.95</td>
                    <td align="right" width="140">233.90</td>
                    <td align="right" width="140">1.32</td>
                    <td align="right" width="140">17,978.95</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/ntpc/NTP" style="text-decoration:none;color:#333333">NTPC</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE733E01010','BSE','532555');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/ntpc-to-start-commercial-operation250-mw-unitbarauni-power-stationmarch-1_13536801.html" title="NTPC to start commercial operation of 250 mw unit of Barauni Power Station from March 1"><span>NTPC to start commercial operation of 250 mw unit of Barauni Power Station from March 1</span></a><em>Feb 28, 11:30</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/ntpc/news/NTP" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">107.00</td>
                    <td align="right" width="130">108.40</td>
                    <td align="right" width="140">1.40</td>
                    <td align="right" width="140">1.31</td>
                    <td align="right" width="140">108.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pumps/yukenindia/YI" style="text-decoration:none;color:#333333">Yuken India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE384C01016','BSE','522108');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Yuken India AGM on Sep 03, 2019||Announcement date: Aug 07, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">499.00</td>
                    <td align="right" width="130">505.55</td>
                    <td align="right" width="140">6.55</td>
                    <td align="right" width="140">1.31</td>
                    <td align="right" width="140">505.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/gssinfotech/GAI05" style="text-decoration:none;color:#333333">GSS Infotech</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE871H01011','BSE','532951');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>GSS Infotech closes below 150-Day Moving Average of 35.47 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">30.80</td>
                    <td align="right" width="130">31.20</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.30</td>
                    <td align="right" width="140">31.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/petrochemicals/goacarbon/GC04" style="text-decoration:none;color:#333333">Goa Carbon</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE426D01013','BSE','509567');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Goa Carbon closes below 50-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">217.45</td>
                    <td align="right" width="130">220.25</td>
                    <td align="right" width="140">2.80</td>
                    <td align="right" width="140">1.29</td>
                    <td align="right" width="140">220.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/chemicals/excelindustries/EI10" style="text-decoration:none;color:#333333">Excel</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE369A01029','BSE','500650');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Excel has hit 52wk low of Rs 659.65 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">662.00</td>
                    <td align="right" width="130">670.50</td>
                    <td align="right" width="140">8.50</td>
                    <td align="right" width="140">1.28</td>
                    <td align="right" width="140">670.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/chalethotels/CH03" style="text-decoration:none;color:#333333">Chalet Hotels</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE427F01016','BSE','542399');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Chalet Hotels closes above 200-Day Moving Average of 329.35 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">325.25</td>
                    <td align="right" width="130">329.40</td>
                    <td align="right" width="140">4.15</td>
                    <td align="right" width="140">1.28</td>
                    <td align="right" width="140">329.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/packaging/garwarepolyester/GP" style="text-decoration:none;color:#333333">Garware Poly</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE291A01017','BSE','500655');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Garware Poly AGM on Sep 25, 2019||Announcement date: Aug 08, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">199.25</td>
                    <td align="right" width="130">201.80</td>
                    <td align="right" width="140">2.55</td>
                    <td align="right" width="140">1.28</td>
                    <td align="right" width="140">201.80</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/diversified/indianenergyexchange/IEE" style="text-decoration:none;color:#333333">IEX</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE022Q01020','BSE','540750');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>IEX closes above 30-Day Moving Average of 179.42 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">185.00</td>
                    <td align="right" width="130">187.35</td>
                    <td align="right" width="140">2.35</td>
                    <td align="right" width="140">1.27</td>
                    <td align="right" width="140">187.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/torrentpower/TP14" style="text-decoration:none;color:#333333">Torrent Power</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE813H01021','BSE','532779');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Torrent Power closes above 30-Day Moving Average of 313.42 today.</span></li><li><span>Torrent Power closes above 50-Day Moving Average of 304.84 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">315.40</td>
                    <td align="right" width="130">319.40</td>
                    <td align="right" width="140">4.00</td>
                    <td align="right" width="140">1.27</td>
                    <td align="right" width="140">319.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textileshosieryknitwear/tt/TT06" style="text-decoration:none;color:#333333">TT</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE592B01016','BSE','514142');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>TT closes above 150-Day Moving Average of 40.29 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">39.75</td>
                    <td align="right" width="130">40.25</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">1.26</td>
                    <td align="right" width="140">40.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/exideindustries/EI" style="text-decoration:none;color:#333333">Exide Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE302A01020','BSE','500086');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Exide Ind Dividend||Interim Dividend 250.00%||Announcement date: Feb 24, 2020||Record date: Mar 05, 2020||Ex-Div: Mar 04, 2020</span></li><li><span>Exide Ind has hit 52wk low of Rs 161.10 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">160.05</td>
                    <td align="right" width="130">162.05</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">1.25</td>
                    <td align="right" width="140">162.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/sinclairshotels/SH11" style="text-decoration:none;color:#333333">Sinclairs Hotel</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE985A01014','BSE','523023');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sinclairs Hotel closes above 50-Day Moving Average of 295.40 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">284.10</td>
                    <td align="right" width="130">287.65</td>
                    <td align="right" width="140">3.55</td>
                    <td align="right" width="140">1.25</td>
                    <td align="right" width="140">287.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/maithanalloys/MA04" style="text-decoration:none;color:#333333">Maithan Alloys</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE683C01011','BSE','590078');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Maithan Alloys closes above 150-Day Moving Average of 484.33 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">490.50</td>
                    <td align="right" width="130">496.60</td>
                    <td align="right" width="140">6.10</td>
                    <td align="right" width="140">1.24</td>
                    <td align="right" width="140">496.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/kaya/K03" style="text-decoration:none;color:#333333">Kaya</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE587G01015','BSE','539276');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kaya has hit 52wk low of Rs 296.45 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">258.00</td>
                    <td align="right" width="130">261.20</td>
                    <td align="right" width="140">3.20</td>
                    <td align="right" width="140">1.24</td>
                    <td align="right" width="140">261.20</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hotels/indianhotelscompany/IHC" style="text-decoration:none;color:#333333">Indian Hotels</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE053A01029','BSE','500850');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Indian Hotels closes below 30-Day,50-Day Moving Average today.</span></li><li><span>Indian Hotels Block Deal on NSE||Qty: 500,077||Deal Price: 136.00||Value (cr): 6.80||Time: 09:24am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">131.25</td>
                    <td align="right" width="130">132.85</td>
                    <td align="right" width="140">1.60</td>
                    <td align="right" width="140">1.22</td>
                    <td align="right" width="140">132.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/iolchemicalspharmaceuticals/IOL01" style="text-decoration:none;color:#333333">IOL Chemicals</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE485C01011','BSE','524164');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in IOL Chemicals on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">218.35</td>
                    <td align="right" width="130">221.00</td>
                    <td align="right" width="140">2.65</td>
                    <td align="right" width="140">1.21</td>
                    <td align="right" width="140">221.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/aplapollotubes/BT09" style="text-decoration:none;color:#333333">APL Apollo</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE702C01019','BSE','533758');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>APL Apollo closes below 30-Day Moving Average of 2011.91 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,890.35</td>
                    <td align="right" width="130">1,913.00</td>
                    <td align="right" width="140">22.65</td>
                    <td align="right" width="140">1.20</td>
                    <td align="right" width="140">1,913.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steelspongeiron/sardaenergyminerals/SEM" style="text-decoration:none;color:#333333">Sarda Energy</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE385C01013','BSE','504614');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Sarda Energy and Minerals' board meeting on August 11, 2018</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/sardaenergyminerals/notices/SEM" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Sarda Energy closes above 200-Day Moving Average of 201.72 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">169.00</td>
                    <td align="right" width="130">171.00</td>
                    <td align="right" width="140">2.00</td>
                    <td align="right" width="140">1.18</td>
                    <td align="right" width="140">171.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autoancillaries/fiemindustries/FIE" style="text-decoration:none;color:#333333">FIEM Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE737H01014','BSE','532768');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>FIEM Ind closes below 50-Day Moving Average of 463.54 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">425.00</td>
                    <td align="right" width="130">430.00</td>
                    <td align="right" width="140">5.00</td>
                    <td align="right" width="140">1.18</td>
                    <td align="right" width="140">430.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesreadymadeapparels/montecarlofashions/MC05" style="text-decoration:none;color:#333333">Monte Carlo</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE950M01013','BSE','538836');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Monte Carlo has hit 52wk low of Rs 201.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">197.00</td>
                    <td align="right" width="130">199.30</td>
                    <td align="right" width="140">2.30</td>
                    <td align="right" width="140">1.17</td>
                    <td align="right" width="140">199.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/transportlogistics/navkarcorporation/NC02" style="text-decoration:none;color:#333333">Navkar Corp</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE278M01019','BSE','539332');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Navkar Corp closes above  its 30-Day,150-Day,200-Day Moving Average today.</span></li><li><span>Navkar Corp closes above  its 30-Day,150-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">25.95</td>
                    <td align="right" width="130">26.25</td>
                    <td align="right" width="140">0.30</td>
                    <td align="right" width="140">1.16</td>
                    <td align="right" width="140">26.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/sugar/dalmiabharatsugarindustries/DCB" style="text-decoration:none;color:#333333">Dalmia Sugar</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE495A01022','BSE','500097');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Dalmia Sugar Dividend||Interim Dividend 100.00%||Announcement date: Feb 13, 2020||Record date: Feb 26, 2020||Ex-Div: Feb 25, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">85.85</td>
                    <td align="right" width="130">86.85</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.16</td>
                    <td align="right" width="140">86.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesmanmade/filatexindia/FI06" style="text-decoration:none;color:#333333">Filatex India</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE816B01027','BSE','526227');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Filatex India closes below 150-Day Moving Average of 38.67 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">34.45</td>
                    <td align="right" width="130">34.85</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.16</td>
                    <td align="right" width="140">34.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cementproductsbuildingmaterials/ramcoindustries/RI26" style="text-decoration:none;color:#333333">Ramcoind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE614A01028','BSE','532369');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ramcoind closes above 150-Day Moving Average of 183.20 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">163.50</td>
                    <td align="right" width="130">165.40</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">1.16</td>
                    <td align="right" width="140">165.40</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/retail/shoppersstop/SS51" style="text-decoration:none;color:#333333">Shoppers Stop</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE498B01024','BSE','532638');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_sppic"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>NEWS</h1>
								<div class="PA10">
								  <ul><li><span><a href="https://www.moneycontrol.com/news/business/shoppers-stop-sees-beauty-space-as-next-growth-driver_13530801.html" title="Shoppers Stop sees beauty space as next growth driver"><span>Shoppers Stop sees beauty space as next growth driver</span></a><em>Feb 26, 06:37</em></span></li></ul>
							<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-article/shoppersstop/news/SS51" title="View all" target="_blank">View all <span class="vieimgnw"></span></a></p>
								</div>
								<span style="left:2px;" class="arrwodn"></span> 
							</div>
						</div></div></td>
                    <td align="right" width="130">375.00</td>
                    <td align="right" width="130">379.30</td>
                    <td align="right" width="140">4.30</td>
                    <td align="right" width="140">1.15</td>
                    <td align="right" width="140">379.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steelspongeiron/godawaripowerispat/GPI7" style="text-decoration:none;color:#333333">Godawari Power</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE177H01013','BSE','532734');"></span><div class="MT5"></div></td>
                    <td align="right" width="130">165.10</td>
                    <td align="right" width="130">167.00</td>
                    <td align="right" width="140">1.90</td>
                    <td align="right" width="140">1.15</td>
                    <td align="right" width="140">167.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/amberenterprisesindialimited/AEI01" style="text-decoration:none;color:#333333">Amber Enterpris</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE371P01015','BSE','540902');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Amber Enterpris closes above 50-Day Moving Average of 1385.41 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,404.65</td>
                    <td align="right" width="130">1,420.65</td>
                    <td align="right" width="140">16.00</td>
                    <td align="right" width="140">1.14</td>
                    <td align="right" width="140">1,420.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/welspunenterprises/MSK" style="text-decoration:none;color:#333333">Welspun Enter</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE625G01013','BSE','532553');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Welspun Enter closes above 50-Day Moving Average of 80.33 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">61.20</td>
                    <td align="right" width="130">61.90</td>
                    <td align="right" width="140">0.70</td>
                    <td align="right" width="140">1.14</td>
                    <td align="right" width="140">61.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/vedanta/SG" style="text-decoration:none;color:#333333">Vedanta</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE205A01025','BSE','500295');"></span><div class="MT5"></div></td>
                    <td align="right" width="130">118.20</td>
                    <td align="right" width="130">119.55</td>
                    <td align="right" width="140">1.35</td>
                    <td align="right" width="140">1.14</td>
                    <td align="right" width="140">119.55</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/steeltubespipes/goodluckindia/GLS" style="text-decoration:none;color:#333333">Good Luck</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE127I01024','BSE','530655');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Good Luck closes below 50-Day Moving Average of 49.83 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">39.40</td>
                    <td align="right" width="130">39.85</td>
                    <td align="right" width="140">0.45</td>
                    <td align="right" width="140">1.14</td>
                    <td align="right" width="140">39.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/castingsforgings/nelcast/N06" style="text-decoration:none;color:#333333">Nelcast</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE189I01024','BSE','532864');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Nelcast closes below 150-Day Moving Average of 45.43 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">35.35</td>
                    <td align="right" width="130">35.75</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.13</td>
                    <td align="right" width="140">35.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/ozoneworld/OW" style="text-decoration:none;color:#333333">Ozone World</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE583K01016','BSE','539291');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Only Sellers in Ozone World on BSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">80.00</td>
                    <td align="right" width="130">80.90</td>
                    <td align="right" width="140">0.90</td>
                    <td align="right" width="140">1.13</td>
                    <td align="right" width="140">80.90</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/fertilisers/nationalfertilizers/NF06" style="text-decoration:none;color:#333333">NFL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE870D01012','BSE','523630');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>NFL closes below 200-Day Moving Average of 30.32 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">22.40</td>
                    <td align="right" width="130">22.65</td>
                    <td align="right" width="140">0.25</td>
                    <td align="right" width="140">1.12</td>
                    <td align="right" width="140">22.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/constructioncontractingcivil/ahluwaliacontractsindia/ACI12" style="text-decoration:none;color:#333333">Ahluwalia</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE758C01029','BSE','532811');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ahluwalia closes above 200-Day Moving Average of 305.44 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">335.00</td>
                    <td align="right" width="130">338.75</td>
                    <td align="right" width="140">3.75</td>
                    <td align="right" width="140">1.12</td>
                    <td align="right" width="140">338.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/leatherproducts/mirzainternational/MI46" style="text-decoration:none;color:#333333">Mirza Intl</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE771A01026','BSE','526642');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Mirza Intl closes below 150-Day Moving Average of 57.58 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">54.65</td>
                    <td align="right" width="130">55.25</td>
                    <td align="right" width="140">0.60</td>
                    <td align="right" width="140">1.10</td>
                    <td align="right" width="140">55.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electricequipment/salzerelectronics/SE01" style="text-decoration:none;color:#333333">Salzer Electro</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE457F01013','BSE','517059');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Salzer Electro closes above 30-Day,150-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">97.00</td>
                    <td align="right" width="130">98.05</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">1.08</td>
                    <td align="right" width="140">98.05</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/electricals/bharatelectronics/BE03" style="text-decoration:none;color:#333333">Bharat Elec</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE263A01024','BSE','500049');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Bharat Elec has hit 52wk low of Rs 72.00 on NSE</span></li><li><span>Bharat Elec has hit 52wk low of Rs 72.75 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">73.90</td>
                    <td align="right" width="130">74.70</td>
                    <td align="right" width="140">0.80</td>
                    <td align="right" width="140">1.08</td>
                    <td align="right" width="140">74.70</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/cigarettes/theindianwoodproductscol/IWP540954" style="text-decoration:none;color:#333333">The Indian Wood</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE586E01020','BSE','540954');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>The Indian Wood closes above 30-Day,50-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">37.10</td>
                    <td align="right" width="130">37.50</td>
                    <td align="right" width="140">0.40</td>
                    <td align="right" width="140">1.08</td>
                    <td align="right" width="140">37.50</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miscellaneous/kaveriseedcompany/KSC01" style="text-decoration:none;color:#333333">Kaveri Seed</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE455I01029','BSE','532899');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kaveri Seed closes below 200-Day Moving Average of 482.46 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">430.40</td>
                    <td align="right" width="130">435.00</td>
                    <td align="right" width="140">4.60</td>
                    <td align="right" width="140">1.07</td>
                    <td align="right" width="140">435.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/ceramicsgranite/hsil/HSI02" style="text-decoration:none;color:#333333">HSIL</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE415A01038','BSE','500187');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>HSIL closes below 50-Day Moving Average of 52.90 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">51.60</td>
                    <td align="right" width="130">52.15</td>
                    <td align="right" width="140">0.55</td>
                    <td align="right" width="140">1.07</td>
                    <td align="right" width="140">52.15</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/computerssoftwaremediumsmall/datamaticsglobalservices/DGS01" style="text-decoration:none;color:#333333">Datamatics Glob</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE365B01017','BSE','532528');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Datamatics Glob has hit 52wk low of Rs 57.00 on NSE</span></li><li><span>Datamatics Glob has hit 52wk low of Rs 57.00 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">56.00</td>
                    <td align="right" width="130">56.60</td>
                    <td align="right" width="140">0.60</td>
                    <td align="right" width="140">1.07</td>
                    <td align="right" width="140">56.60</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesreadymadeapparels/pageindustries/PI35" style="text-decoration:none;color:#333333">Page Industries</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE761H01022','BSE','532827');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Page Industries closes above 150-Day Moving Average of 21908.35 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">21,947.70</td>
                    <td align="right" width="130">22,182.85</td>
                    <td align="right" width="140">235.15</td>
                    <td align="right" width="140">1.07</td>
                    <td align="right" width="140">22,182.85</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/autocarsjeeps/mahindramahindra/MM" style="text-decoration:none;color:#333333">M&amp;M</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE101A01026','BSE','500520');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>M&amp;M has hit 52wk low of Rs 452.50 on NSE</span></li><li><span>M&amp;M has hit 52wk low of Rs 452.50 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">462.80</td>
                    <td align="right" width="130">467.65</td>
                    <td align="right" width="140">4.85</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">467.65</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/edibleoilssolventextraction/gujaratambujaexports/GAE" style="text-decoration:none;color:#333333">Guj Amb Exports</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE036B01022','BSE','524226');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Guj Amb Exports closes above 30-Day,200-Day Moving Average today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">157.60</td>
                    <td align="right" width="130">159.25</td>
                    <td align="right" width="140">1.65</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">159.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/aquaculture/kingsinfraventures/VAF01" style="text-decoration:none;color:#333333">Kings Infra</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE050N01010','BSE','530215');"></span><div class="MT5"><div class="disin PR tolhov">
					<span class="ic_vol ML5"></span>
						<div class="stagetool tooltip1 PB5 dnone">
							<h1>ANNOUNCEMENTS</h1>
							<div class="PA10">
							  <ul><li><a href="javascript:void(0)"><span>Kings Infra Ventures' board meeting on December 09, 2017</span></a></li><li><a href="javascript:void(0)"><span>Kings Infra Ventures' appoints Meera Cyriac Company Secretary &amp; CO</span></a></li></ul>
						<p><a class="viewall_bk" href="http://www.moneycontrol.com/company-notices/kingsinfraventures/notices/VAF01" target="_blank">View all <span class="vieimgnw"></span></a></p>
							</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Kings Infra closes below 50-Day Moving Average of 24.07 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">23.75</td>
                    <td align="right" width="130">24.00</td>
                    <td align="right" width="140">0.25</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">24.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/engineering/permanentmagnets/PM01" style="text-decoration:none;color:#333333">Permanent Magne</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE418E01018','BSE','504132');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Permanent Magne AGM on Sep 28, 2019||Announcement date: Aug 29, 2019</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">95.00</td>
                    <td align="right" width="130">96.00</td>
                    <td align="right" width="140">1.00</td>
                    <td align="right" width="140">1.05</td>
                    <td align="right" width="140">96.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/hospitalsmedicalservices/metropolishealthcare/MH06" style="text-decoration:none;color:#333333">Metropolis</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE112L01020','BSE','542650');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Metropolis Dividend||Interim Dividend 400.00%||Announcement date: Feb 06, 2020||Record date: Feb 15, 2020||Ex-Div: Feb 13, 2020</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">1,992.40</td>
                    <td align="right" width="130">2,013.00</td>
                    <td align="right" width="140">20.60</td>
                    <td align="right" width="140">1.03</td>
                    <td align="right" width="140">2,013.00</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/aluminium/nationalaluminiumcompany/NAC" style="text-decoration:none;color:#333333">NALCO</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE139A01034','BSE','532234');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>NALCO Block Deal on BSE||Qty: 592,049||Deal Price: 36.85||Value (cr): 2.18||Time: 09:35am</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">33.90</td>
                    <td align="right" width="130">34.25</td>
                    <td align="right" width="140">0.35</td>
                    <td align="right" width="140">1.03</td>
                    <td align="right" width="140">34.25</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/textilesgeneral/shivamillslimited/SHIVA54096" style="text-decoration:none;color:#333333">Shiva Mills Lim</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE644Y01017','BSE','540961');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Shiva Mills Lim closes below 50-Day Moving Average of 31.46 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">29.05</td>
                    <td align="right" width="130">29.35</td>
                    <td align="right" width="140">0.30</td>
                    <td align="right" width="140">1.03</td>
                    <td align="right" width="140">29.35</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/consumergoodswhitegoods/johnsoncontrolshitachiairconditioningindia/HHL" style="text-decoration:none;color:#333333">Johnson Control</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE782A01015','BSE','523398');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Johnson Control closes above 50-Day Moving Average of 1948.57 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">2,960.00</td>
                    <td align="right" width="130">2,990.10</td>
                    <td align="right" width="140">30.10</td>
                    <td align="right" width="140">1.02</td>
                    <td align="right" width="140">2,990.10</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/miningminerals/gujaratmineraldevelopmentcorporation/GMD" style="text-decoration:none;color:#333333">Guj Mineral</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE131A01031','BSE','532181');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Guj Mineral has hit 52wk low of Rs 50.50 on NSE</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">48.80</td>
                    <td align="right" width="130">49.30</td>
                    <td align="right" width="140">0.50</td>
                    <td align="right" width="140">1.02</td>
                    <td align="right" width="140">49.30</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/castingsforgings/ramkrishnaforgings/RF17" style="text-decoration:none;color:#333333">RamkrishnaForge</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE399G01015','BSE','532527');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>RamkrishnaForge closes below 50-Day Moving Average of 356.68 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">272.00</td>
                    <td align="right" width="130">274.75</td>
                    <td align="right" width="140">2.75</td>
                    <td align="right" width="140">1.01</td>
                    <td align="right" width="140">274.75</td>
                  </tr>
                                    <tr>
                    <td class="PR" width="215"><span class="gld13 disin"><a href="https://www.moneycontrol.com/india/stockpricequote/packaging/esterindustries/EI20" style="text-decoration:none;color:#333333">Ester Ind</a>
                                            <div class="disin PR tipshow"><span class="ic_plusor"></span>
                        <div class="stagetool wd190 dnone">
                          <div class="PA5 CTR op_gl12">Add to</div>
                          <div class="add_bubg CTR"> <a href="javascript:;" onclick="javascript:chkbx_val('PP19','1');" class="bl13 watch"><span class="ic_watchlist"></span>Watchlist</a> | <a href="javascript:;" onclick="javascript:chkbx_val('PP19','5');" class="bl13 port"><span class="ic_portfolio"></span>Portfolio</a> </div>
                          <span class="arrwodn"></span> </div>
                      </div>
					                        </span> <span class="ic_tradenwicn btn_tradep_pop ML2" onclick="tradepopup('INE778B01029','BSE','500136');"></span><div class="MT5"><div class="disin PR tolhov">
						<span class="ic_graphsp ML5"></span>
							<div class="stagetool tooltip1 PB5 dnone">
								<h1>ACTIONS</h1>
								<div class="PA10">
								  <ul><li><span>Ester Ind closes above 50-Day Moving Average of 37.42 today.</span></li></ul>
						</div>
							<span style="left:2px;" class="arrwodn"></span> 
						</div>
					</div></div></td>
                    <td align="right" width="130">34.80</td>
                    <td align="right" width="130">35.15</td>
                    <td align="right" width="140">0.35</td>
                    <td align="right" width="140">1.01</td>
                    <td align="right" width="140">35.15</td>
                  </tr>
                  	 
                </tbody>
              </table>''', 'html.parser')

body = soup.find("tbody")

rows = body.find_all("tr")

data = [[cell.find("a").text if cell.find(["a", ""]) != None else cell.text for cell in row.find_all(["th", "td"])] for row in body.find_all("tr")]
