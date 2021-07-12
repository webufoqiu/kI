JQData：
包括沪深A股行情数据，上市公司财务数据，场内基金数据，场外基金数据，指数数据，期货数据，期权数据、债券数据以及宏观经济数据



```python
pip install jqdatasdk -i https://pypi.tuna.tsinghua.edu.cn/simple
import jqdatasdk
jqdatasdk.auth(‘username’, ‘password’) # 填写自己的

import jqdatasdk
jqdatasdk.auth('13282159964', '159964')
```



# 获取平安银行股票数据
```python
jqdatasdk.get_price("000001.XSHE", start_date="2021-01-01", end_date="2021-03-05")
```

