Feature: 登录IMP平台

  Scenario: 用户输入正确的账户和密码进行登录
    Given 打开浏览器且进入登录页面
    When 输入账号:heyeping
    And 输入密码:abc@1234
    And 点击登录按钮
    Then 登录成功