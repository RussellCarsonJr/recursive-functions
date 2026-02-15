# test_functions.py
import sys

def test_mult_recur():
    from mult_recur import mult_recur
    
    # Test positive multiplication
    assert mult_recur(3, 4) == 12, "3 * 4 should equal 12"
    assert mult_recur(5, 1) == 5, "5 * 1 should equal 5"
    assert mult_recur(7, 2) == 14, "7 * 2 should equal 14"
    print("✓ mult_recur tests passed!")

def test_power_recur():
    from power_recur import power_recur
    
    # Test positive exponents
    assert power_recur(2, 3) == 8, "2^3 should equal 8"
    assert power_recur(5, 2) == 25, "5^2 should equal 25"
    
    # Test base cases
    assert power_recur(10, 0) == 1, "10^0 should equal 1"
    assert power_recur(7, 1) == 7, "7^1 should equal 7"
    
    # Test negative exponents
    assert power_recur(2, -1) == 0.5, "2^-1 should equal 0.5"
    assert power_recur(2, -2) == 0.25, "2^-2 should equal 0.25"
    assert abs(power_recur(2, -3) - 0.125) < 0.001, "2^-3 should equal 0.125"
    
    print("✓ power_recur tests passed!")

def test_fact_recur():
    from fact_recur import fact_recur
    
    # Test positive factorials
    assert fact_recur(0) == 1, "0! should equal 1"
    assert fact_recur(1) == 1, "1! should equal 1"
    assert fact_recur(4) == 24, "4! should equal 24"
    assert fact_recur(5) == 120, "5! should equal 120"
    
    # Test negative (should raise error)
    try:
        fact_recur(-1)
        assert False, "fact_recur(-1) should raise ValueError"
    except ValueError:
        pass  # Expected behavior
    
    print("✓ fact_recur tests passed!")

if __name__ == "__main__":
    try:
        test_mult_recur()
        test_power_recur()
        test_fact_recur()
        print("\n🎉 All tests passed!")
        sys.exit(0)  # Success
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)  # Failure
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)  # Failure