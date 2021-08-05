# Generated from Json.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonParser import JsonParser
else:
    from JsonParser import JsonParser

# This class defines a complete listener for a parse tree produced by JsonParser.
class JsonListener(ParseTreeListener):

    # Enter a parse tree produced by JsonParser#json.
    def enterJson(self, ctx:JsonParser.JsonContext):
        pass

    # Exit a parse tree produced by JsonParser#json.
    def exitJson(self, ctx:JsonParser.JsonContext):
        pass


    # Enter a parse tree produced by JsonParser#object.
    def enterObject(self, ctx:JsonParser.ObjectContext):
        pass

    # Exit a parse tree produced by JsonParser#object.
    def exitObject(self, ctx:JsonParser.ObjectContext):
        pass


    # Enter a parse tree produced by JsonParser#pair.
    def enterPair(self, ctx:JsonParser.PairContext):
        pass

    # Exit a parse tree produced by JsonParser#pair.
    def exitPair(self, ctx:JsonParser.PairContext):
        pass


    # Enter a parse tree produced by JsonParser#pairValues.
    def enterPairValues(self, ctx:JsonParser.PairValuesContext):
        pass

    # Exit a parse tree produced by JsonParser#pairValues.
    def exitPairValues(self, ctx:JsonParser.PairValuesContext):
        pass


    # Enter a parse tree produced by JsonParser#array.
    def enterArray(self, ctx:JsonParser.ArrayContext):
        pass

    # Exit a parse tree produced by JsonParser#array.
    def exitArray(self, ctx:JsonParser.ArrayContext):
        pass


    # Enter a parse tree produced by JsonParser#value.
    def enterValue(self, ctx:JsonParser.ValueContext):
        pass

    # Exit a parse tree produced by JsonParser#value.
    def exitValue(self, ctx:JsonParser.ValueContext):
        pass


    # Enter a parse tree produced by JsonParser#function.
    def enterFunction(self, ctx:JsonParser.FunctionContext):
        pass

    # Exit a parse tree produced by JsonParser#function.
    def exitFunction(self, ctx:JsonParser.FunctionContext):
        pass


    # Enter a parse tree produced by JsonParser#argument.
    def enterArgument(self, ctx:JsonParser.ArgumentContext):
        pass

    # Exit a parse tree produced by JsonParser#argument.
    def exitArgument(self, ctx:JsonParser.ArgumentContext):
        pass


    # Enter a parse tree produced by JsonParser#functionName.
    def enterFunctionName(self, ctx:JsonParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by JsonParser#functionName.
    def exitFunctionName(self, ctx:JsonParser.FunctionNameContext):
        pass



del JsonParser