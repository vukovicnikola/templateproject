import templateproject

def main():
    import sys
    arg1 = sys.argv[1]
    templateproject.init_proj(arg1)
    
if __name__ == "__main__":
    main()