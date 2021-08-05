# Generated from Json.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonParser import JsonParser
else:
    from JsonParser import JsonParser

# This class defines a complete generic visitor for a parse tree produced by JsonParser.

class JsonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JsonParser#json.
    def visitJson(self, ctx:JsonParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#object.
    def visitObject(self, ctx:JsonParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#pair.
    def visitPair(self, ctx:JsonParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#pairValues.
    def visitPairValues(self, ctx:JsonParser.PairValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#array.
    def visitArray(self, ctx:JsonParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#value.
    def visitValue(self, ctx:JsonParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#function.
    def visitFunction(self, ctx:JsonParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#argument.
    def visitArgument(self, ctx:JsonParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonParser#functionName.
    def visitFunctionName(self, ctx:JsonParser.FunctionNameContext):
        return self.visitChildren(ctx)



del JsonParser