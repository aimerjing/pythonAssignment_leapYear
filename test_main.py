# 这是测试文件，用于平台自动评分，不要修改其代码
import subprocess
import sys

def run_program(input_value):
    """运行学生程序并捕获输出"""
    try:
        process = subprocess.run(
            [sys.executable, "main.py"],
            input=f"{input_value}\n",
            text=True,
            capture_output=True,
            timeout=5
        )
        return process.stdout, process.stderr
    except Exception as e:
        return "", str(e)

def test_leap_year():
    """主测试函数"""
    test_cases = [
        # 闰年测试
        ("2000", "是闰年"),   # 能被400整除
        ("2004", "是闰年"),   # 能被4整除但不能被100整除
        ("2400", "是闰年"),   # 能被400整除
        
        # 非闰年测试
        ("1900", "不是闰年"), # 能被100整除但不能被400整除
        ("2001", "不是闰年"), # 不能被4整除
        ("2100", "不是闰年"), # 能被100整除但不能被400整除
        
        # 边界值测试
        ("0", "是闰年"),      # 公元0年是闰年
        ("-100", "不是闰年"), # 负年份处理
        
        # 无效输入测试
        ("abc", "输入错误"),  # 非数字输入
        ("", "输入错误"),     # 空输入
        ("2023.5", "输入错误") # 浮点数输入
    ]
    
    passed = 0
    total = len(test_cases)
    
    for input_val, expected in test_cases:
        stdout, stderr = run_program(input_val)
        output = stdout.strip()
        
        # 检查输出是否包含预期关键字
        if expected in output:
            print(f"✅ 测试通过: {input_val} -> {expected}")
            passed += 1
        else:
            print(f"❌ 测试失败: {input_val}")
            print(f"   预期输出应包含: '{expected}'")
            print(f"   实际输出: '{output}'")
    
    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试通过!")
        exit(0)
    else:
        print("💥 存在未通过的测试")
        exit(1)

if __name__ == "__main__":
    test_leap_year()
