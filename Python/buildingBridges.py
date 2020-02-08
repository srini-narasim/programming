from lineSegments import *
from bridgeParts import * 

def showSingleSpanHeavyRoadwayBridge():
	print "Single Span, Heavy Roadway Bridge"
	print line_segment_of_equals() * 3
	print singleSpanSupportLayer()
	print singleSpanSupportLayer()
	print singleSpanSupportLayer()

def showSingleSpanLightRoadwayBridge():
	print "Single Span, Light Roadway Bridge"
	print line_segment_of_hyphens() * 3
	print singleSpanSupportLayer()
	print singleSpanSupportLayer()
	print singleSpanSupportLayer()

def showDoubleSpanLightRoadwayBridge():
	print "Double Span, Light Roadway Bridge"
	print line_segment_of_hyphens() * 5
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()


def showDoubleSpanHeavyRoadwayBridge():
	print "Double Span, Heavy Roadway Bridge"
	print line_segment_of_equals() * 5
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()
	print singleSpanSupportLayer() + line_segment_of_spaces() + line_segment_of_Xs()



def showDifferentBridges():
	showSingleSpanLightRoadwayBridge()
	showSingleSpanHeavyRoadwayBridge()
	showDoubleSpanLightRoadwayBridge()
	showDoubleSpanHeavyRoadwayBridge()

showDifferentBridges()




