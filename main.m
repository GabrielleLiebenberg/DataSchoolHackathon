pyrunfile('main.py');
 %opts = detectImportOptions("restaurant1_avg_data.csv");
% %getvaropts(opts,'date');
 %opts = setvaropts(opts,'date','DatetimeFormat','yyyy-MM-dd');
%2015-09-2
%[Date, ItemName, Quantity, ProductPrice, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff]= importfile1("restaurant1_data.csv", [2, Inf]);
%restaurant1_data = table(Date, ItemName, Quantity, ProductPrice, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff);
%restaurant1_data = importfile1("restaurant1_data.csv", [2, Inf]);
%restaurant2_data = importfile1("restaurant2_data.csv", [2, Inf]);

%[Var1, OrderDate, ItemName, Quantity, ProductPrice, TotalProducts, date, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff] = importfilecolumns("restaurant1_data.csv", [1, Inf]);
%restaurant1_data = table(Var1, OrderDate, ItemName, Quantity, ProductPrice, TotalProducts, date, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff);

%[tdate, tItemName, tQuantity, tProductPrice, tcloud_cover, tsunshine, tglobal_radiation, tmax_temp, tmean_temp, tmin_temp, tprecipitation, tpressure, tsnow_depth, tisPaidTimeOff] = importfileAVGcols("restaurant1_avg_data.csv", [1, Inf]);
[Var1, OrderNumber, OrderDate, ItemName, Quantity, ProductPrice, TotalProducts, date, day, month, year, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff] = importfileCols("restaurant1_data.csv", [2, Inf]);
restaurant1_data = table(Var1, OrderNumber, OrderDate, ItemName, Quantity, ProductPrice, TotalProducts, date, day, month, year, cloud_cover, sunshine, global_radiation, max_temp, mean_temp, min_temp, precipitation, pressure, snow_depth, isPaidTimeOff);

[tdate, tItemName, tQuantity, tday, tmonth, tyear, tProductPrice, tcloud_cover, tsunshine, tglobal_radiation, tmax_temp, tmean_temp, tmin_temp, tprecipitation, tpressure, tsnow_depth, tisPaidTimeOff] = importfileAVGcols("restaurant1_avg_data.csv", [2, Inf]);
restaurant1_avg_data = table(tdate, tItemName, tQuantity, tday, tmonth, tyear, tProductPrice, tcloud_cover, tsunshine, tglobal_radiation, tmax_temp, tmean_temp, tmin_temp, tprecipitation, tpressure, tsnow_depth, tisPaidTimeOff);


%train model
[trainedModel, validationRMSE] = trainRegressionModel1(restaurant1_data);

%generate prediction
pred = trainedModel.predictFcn(restaurant1_data);
% 
% 
% %plot('date', pred, ".")
% plot3(ItemName, Quantity, pred, ".")
% grid on