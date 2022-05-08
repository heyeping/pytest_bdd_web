Feature: 测试百度搜索

  Scenario: 访问百度并搜索关键字
    Given 访问百度首页
    When 输入关键字:hyp
    And 点击搜索按钮
    Then 验证返回的搜索结果标题:hyp_百度搜索