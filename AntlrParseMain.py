from antlr4 import *

from antlr.JsonLexer import JsonLexer
from antlr.JsonParser import JsonParser

from antlr.JsonListener import JsonListener

class ConcreteJsonListener(JsonListener):

    def enterFunction(self, ctx: JsonParser.FunctionContext):
        print("ctx.functionName(): " + ctx.functionName().__str__())


def main():
    parsed_string = """{"name":"value" + str($name(str))}"""
    print("parsed_string: " + parsed_string)

    # 1. 构建字符输入流
    input_stream = InputStream(parsed_string)

    # 2. 构建词法解析器
    lexer = JsonLexer(input_stream)

    # 3. 构建token流
    token_stream = CommonTokenStream(lexer)

    # 4. 构建语法解析器
    parser = JsonParser(token_stream)

    # 5. 构建语法树遍历器
    parse_tree = ParseTreeWalker()

    # 6. 构建listener
    listener = ConcreteJsonListener()

    # 测试输出语法树
    # print(parser.json().toStringTree()); print("\n")

    # ([]([18] {([27 18] " name ": ([45 27 18] " ([52 45 27 18] value) " + ([61 45 27 18] ([114 61 45 27 18] str)(
    #     ([116 61 45 27 18]([102 116 61 45 27 18] $ name)(([104 116 61 45 27 18] str))) ))))}))

    # 7. 进行listener遍历操作
    parse_tree.walk(listener, parser.json())


if __name__ == "__main__":
    main()
