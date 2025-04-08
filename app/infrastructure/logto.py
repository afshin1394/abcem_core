from typing import Union

from logto import LogtoClient, LogtoConfig, Storage


client = LogtoClient(
    LogtoConfig(
        endpoint="http://localhost:3001/",
        appId="dp24nk69mo59lwslqwlig",
        appSecret="KeouhtEnxJcfmeZYn1SMxW73O1eH3wTy",
    )
)
