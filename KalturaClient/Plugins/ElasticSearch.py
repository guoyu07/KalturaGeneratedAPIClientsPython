# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2018  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from .Core import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaESearchItemType(object):
    EXACT_MATCH = 1
    PARTIAL = 2
    STARTS_WITH = 3
    EXISTS = 4
    RANGE = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchOperatorType(object):
    AND_OP = 1
    OR_OP = 2
    NOT_OP = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionFieldName(object):
    CONTENT = "content"
    END_TIME = "end_time"
    START_TIME = "start_time"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryEntryFieldName(object):
    ANCESTOR_ID = "ancestor_id"
    ANCESTOR_NAME = "ancestor_name"
    FULL_IDS = "full_ids"
    ID = "id"
    NAME = "name"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryFieldName(object):
    CONTRIBUTION_POLICY = "contribution_policy"
    CREATED_AT = "created_at"
    DEPTH = "depth"
    DESCRIPTION = "description"
    DIRECT_ENTRIES_COUNT = "direct_entries_count"
    DIRECT_SUB_CATEGORIES_COUNT = "direct_sub_categories_count"
    DISPLAY_IN_SEARCH = "display_in_search"
    ENTRIES_COUNT = "entries_count"
    FULL_IDS = "full_ids"
    FULL_NAME = "full_name"
    ID = "id"
    INHERITANCE_TYPE = "inheritance_type"
    INHERITED_PARENT_ID = "inherited_parent_id"
    MEMBERS_COUNT = "members_count"
    MODERATION = "moderation"
    NAME = "name"
    PARENT_ID = "parent_id"
    PENDING_ENTRIES_COUNT = "pending_entries_count"
    PENDING_MEMBERS_COUNT = "pending_members_count"
    PRIVACY = "privacy"
    PRIVACY_CONTEXT = "privacy_context"
    PRIVACY_CONTEXTS = "privacy_contexts"
    REFERENCE_ID = "reference_id"
    TAGS = "tags"
    UPDATED_AT = "updated_at"
    USER_ID = "user_id"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryOrderByFieldName(object):
    CREATED_AT = "created_at"
    ENTRIES_COUNT = "entries_count"
    MEMBERS_COUNT = "members_count"
    NAME = "name"
    UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryUserFieldName(object):
    USER_ID = "user_id"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointFieldName(object):
    ANSWERS = "answers"
    END_TIME = "end_time"
    EXPLANATION = "explanation"
    HINT = "hint"
    ID = "id"
    NAME = "name"
    QUESTION = "question"
    START_TIME = "start_time"
    SUB_TYPE = "sub_type"
    TAGS = "tags"
    TEXT = "text"
    TYPE = "type"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchEntryFieldName(object):
    ACCESS_CONTROL_ID = "access_control_id"
    ADMIN_TAGS = "admin_tags"
    CONVERSION_PROFILE_ID = "conversion_profile_id"
    CREATED_AT = "created_at"
    CREATOR_ID = "creator_kuser_id"
    CREDIT = "credit"
    DESCRIPTION = "description"
    END_DATE = "end_date"
    ENTITLED_USER_EDIT = "entitled_kusers_edit"
    ENTITLED_USER_PUBLISH = "entitled_kusers_publish"
    ENTRY_TYPE = "entry_type"
    EXTERNAL_SOURCE_TYPE = "external_source_type"
    ID = "id"
    IS_LIVE = "is_live"
    IS_QUIZ = "is_quiz"
    USER_ID = "kuser_id"
    LENGTH_IN_MSECS = "length_in_msecs"
    MEDIA_TYPE = "media_type"
    MODERATION_STATUS = "moderation_status"
    NAME = "name"
    PARENT_ENTRY_ID = "parent_id"
    PUSH_PUBLISH = "push_publish"
    RECORDED_ENTRY_ID = "recorded_entry_id"
    REDIRECT_ENTRY_ID = "redirect_entry_id"
    REFERENCE_ID = "reference_id"
    ROOT_ID = "root_id"
    SITE_URL = "site_url"
    SOURCE_TYPE = "source_type"
    START_DATE = "start_date"
    TAGS = "tags"
    TEMPLATE_ENTRY_ID = "template_entry_id"
    UPDATED_AT = "updated_at"
    USER_NAMES = "user_names"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchEntryOrderByFieldName(object):
    CREATED_AT = "created_at"
    END_DATE = "end_date"
    LAST_PLAYED_AT = "last_played_at"
    NAME = "name"
    PLAYS = "plays"
    START_DATE = "start_date"
    UPDATED_AT = "updated_at"
    VIEWS = "views"
    VOTES = "votes"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchSortOrder(object):
    ORDER_BY_ASC = "asc"
    ORDER_BY_DESC = "desc"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchUserFieldName(object):
    CREATED_AT = "created_at"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    GROUP_IDS = "group_ids"
    LAST_NAME = "last_name"
    PERMISSION_NAMES = "permission_names"
    ROLE_IDS = "role_ids"
    SCREEN_NAME = "screen_name"
    TAGS = "tags"
    UPDATED_AT = "updated_at"
    TYPE = "user_type"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchUserOrderByFieldName(object):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaESearchBaseItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryBaseItem(KalturaESearchBaseItem):
    def __init__(self):
        KalturaESearchBaseItem.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryBaseItem(KalturaESearchBaseItem):
    def __init__(self):
        KalturaESearchBaseItem.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryBaseNestedObject(KalturaESearchEntryBaseItem):
    def __init__(self):
        KalturaESearchEntryBaseItem.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchEntryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryBaseNestedObject.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryBaseNestedObject")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryNestedBaseItem(KalturaESearchEntryBaseNestedObject):
    def __init__(self):
        KalturaESearchEntryBaseNestedObject.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchEntryBaseNestedObject.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryNestedBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryBaseNestedObject.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryNestedBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchHighlight(KalturaObjectBase):
    def __init__(self,
            fieldName=NotImplemented,
            hits=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.fieldName = fieldName

        # @var array of KalturaString
        self.hits = hits


    PROPERTY_LOADERS = {
        'fieldName': getXmlNodeText, 
        'hits': (KalturaObjectFactory.createArray, 'KalturaString'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHighlight.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchHighlight")
        kparams.addStringIfDefined("fieldName", self.fieldName)
        kparams.addArrayIfDefined("hits", self.hits)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName

    def getHits(self):
        return self.hits

    def setHits(self, newHits):
        self.hits = newHits


# @package Kaltura
# @subpackage Client
class KalturaESearchItemData(KalturaObjectBase):
    def __init__(self,
            highlight=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaESearchHighlight
        self.highlight = highlight


    PROPERTY_LOADERS = {
        'highlight': (KalturaObjectFactory.createArray, 'KalturaESearchHighlight'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchItemData")
        kparams.addArrayIfDefined("highlight", self.highlight)
        return kparams

    def getHighlight(self):
        return self.highlight

    def setHighlight(self, newHighlight):
        self.highlight = newHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchItemDataResult(KalturaObjectBase):
    def __init__(self,
            totalCount=NotImplemented,
            items=NotImplemented,
            itemsType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.totalCount = totalCount

        # @var array of KalturaESearchItemData
        self.items = items

        # @var string
        self.itemsType = itemsType


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
        'items': (KalturaObjectFactory.createArray, 'KalturaESearchItemData'), 
        'itemsType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchItemDataResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchItemDataResult")
        kparams.addIntIfDefined("totalCount", self.totalCount)
        kparams.addArrayIfDefined("items", self.items)
        kparams.addStringIfDefined("itemsType", self.itemsType)
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount

    def getItems(self):
        return self.items

    def setItems(self, newItems):
        self.items = newItems

    def getItemsType(self):
        return self.itemsType

    def setItemsType(self, newItemsType):
        self.itemsType = newItemsType


# @package Kaltura
# @subpackage Client
class KalturaESearchOrderByItem(KalturaObjectBase):
    def __init__(self,
            sortOrder=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaESearchSortOrder
        self.sortOrder = sortOrder


    PROPERTY_LOADERS = {
        'sortOrder': (KalturaEnumsFactory.createString, "KalturaESearchSortOrder"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchOrderByItem")
        kparams.addStringEnumIfDefined("sortOrder", self.sortOrder)
        return kparams

    def getSortOrder(self):
        return self.sortOrder

    def setSortOrder(self, newSortOrder):
        self.sortOrder = newSortOrder


# @package Kaltura
# @subpackage Client
class KalturaESearchOrderBy(KalturaObjectBase):
    def __init__(self,
            orderItems=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaESearchOrderByItem
        self.orderItems = orderItems


    PROPERTY_LOADERS = {
        'orderItems': (KalturaObjectFactory.createArray, 'KalturaESearchOrderByItem'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchOrderBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchOrderBy")
        kparams.addArrayIfDefined("orderItems", self.orderItems)
        return kparams

    def getOrderItems(self):
        return self.orderItems

    def setOrderItems(self, newOrderItems):
        self.orderItems = newOrderItems


# @package Kaltura
# @subpackage Client
class KalturaESearchParams(KalturaObjectBase):
    def __init__(self,
            objectStatuses=NotImplemented,
            objectId=NotImplemented,
            orderBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.objectStatuses = objectStatuses

        # @var string
        self.objectId = objectId

        # @var KalturaESearchOrderBy
        self.orderBy = orderBy


    PROPERTY_LOADERS = {
        'objectStatuses': getXmlNodeText, 
        'objectId': getXmlNodeText, 
        'orderBy': (KalturaObjectFactory.create, 'KalturaESearchOrderBy'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchParams")
        kparams.addStringIfDefined("objectStatuses", self.objectStatuses)
        kparams.addStringIfDefined("objectId", self.objectId)
        kparams.addObjectIfDefined("orderBy", self.orderBy)
        return kparams

    def getObjectStatuses(self):
        return self.objectStatuses

    def setObjectStatuses(self, newObjectStatuses):
        self.objectStatuses = newObjectStatuses

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy


# @package Kaltura
# @subpackage Client
class KalturaESearchRange(KalturaObjectBase):
    def __init__(self,
            greaterThanOrEqual=NotImplemented,
            lessThanOrEqual=NotImplemented,
            greaterThan=NotImplemented,
            lessThan=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.greaterThanOrEqual = greaterThanOrEqual

        # @var int
        self.lessThanOrEqual = lessThanOrEqual

        # @var int
        self.greaterThan = greaterThan

        # @var int
        self.lessThan = lessThan


    PROPERTY_LOADERS = {
        'greaterThanOrEqual': getXmlNodeInt, 
        'lessThanOrEqual': getXmlNodeInt, 
        'greaterThan': getXmlNodeInt, 
        'lessThan': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchRange.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchRange")
        kparams.addIntIfDefined("greaterThanOrEqual", self.greaterThanOrEqual)
        kparams.addIntIfDefined("lessThanOrEqual", self.lessThanOrEqual)
        kparams.addIntIfDefined("greaterThan", self.greaterThan)
        kparams.addIntIfDefined("lessThan", self.lessThan)
        return kparams

    def getGreaterThanOrEqual(self):
        return self.greaterThanOrEqual

    def setGreaterThanOrEqual(self, newGreaterThanOrEqual):
        self.greaterThanOrEqual = newGreaterThanOrEqual

    def getLessThanOrEqual(self):
        return self.lessThanOrEqual

    def setLessThanOrEqual(self, newLessThanOrEqual):
        self.lessThanOrEqual = newLessThanOrEqual

    def getGreaterThan(self):
        return self.greaterThan

    def setGreaterThan(self, newGreaterThan):
        self.greaterThan = newGreaterThan

    def getLessThan(self):
        return self.lessThan

    def setLessThan(self, newLessThan):
        self.lessThan = newLessThan


# @package Kaltura
# @subpackage Client
class KalturaESearchResult(KalturaObjectBase):
    def __init__(self,
            highlight=NotImplemented,
            itemsData=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaESearchHighlight
        self.highlight = highlight

        # @var array of KalturaESearchItemDataResult
        self.itemsData = itemsData


    PROPERTY_LOADERS = {
        'highlight': (KalturaObjectFactory.createArray, 'KalturaESearchHighlight'), 
        'itemsData': (KalturaObjectFactory.createArray, 'KalturaESearchItemDataResult'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchResult")
        kparams.addArrayIfDefined("highlight", self.highlight)
        kparams.addArrayIfDefined("itemsData", self.itemsData)
        return kparams

    def getHighlight(self):
        return self.highlight

    def setHighlight(self, newHighlight):
        self.highlight = newHighlight

    def getItemsData(self):
        return self.itemsData

    def setItemsData(self, newItemsData):
        self.itemsData = newItemsData


# @package Kaltura
# @subpackage Client
class KalturaESearchResponse(KalturaObjectBase):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.totalCount = totalCount

        # @var array of KalturaESearchResult
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
        'objects': (KalturaObjectFactory.createArray, 'KalturaESearchResult'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchResponse")
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaESearchUserBaseItem(KalturaESearchBaseItem):
    def __init__(self):
        KalturaESearchBaseItem.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            line=NotImplemented,
            startsAt=NotImplemented,
            endsAt=NotImplemented,
            language=NotImplemented,
            captionAssetId=NotImplemented,
            label=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.line = line

        # @var int
        self.startsAt = startsAt

        # @var int
        self.endsAt = endsAt

        # @var string
        self.language = language

        # @var string
        self.captionAssetId = captionAssetId

        # @var string
        self.label = label


    PROPERTY_LOADERS = {
        'line': getXmlNodeText, 
        'startsAt': getXmlNodeInt, 
        'endsAt': getXmlNodeInt, 
        'language': getXmlNodeText, 
        'captionAssetId': getXmlNodeText, 
        'label': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCaptionItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchCaptionItemData")
        kparams.addStringIfDefined("line", self.line)
        kparams.addIntIfDefined("startsAt", self.startsAt)
        kparams.addIntIfDefined("endsAt", self.endsAt)
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("captionAssetId", self.captionAssetId)
        kparams.addStringIfDefined("label", self.label)
        return kparams

    def getLine(self):
        return self.line

    def setLine(self, newLine):
        self.line = newLine

    def getStartsAt(self):
        return self.startsAt

    def setStartsAt(self, newStartsAt):
        self.startsAt = newStartsAt

    def getEndsAt(self):
        return self.endsAt

    def setEndsAt(self, newEndsAt):
        self.endsAt = newEndsAt

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getCaptionAssetId(self):
        return self.captionAssetId

    def setCaptionAssetId(self, newCaptionAssetId):
        self.captionAssetId = newCaptionAssetId

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchCategoryOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchCategoryOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryOperator(KalturaESearchCategoryBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchCategoryBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchCategoryBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchCategoryBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchCategoryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchCategoryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryOperator")
        kparams.addIntEnumIfDefined("operator", self.operator)
        kparams.addArrayIfDefined("searchItems", self.searchItems)
        return kparams

    def getOperator(self):
        return self.operator

    def setOperator(self, newOperator):
        self.operator = newOperator

    def getSearchItems(self):
        return self.searchItems

    def setSearchItems(self, newSearchItems):
        self.searchItems = newSearchItems


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryParams(KalturaESearchParams):
    def __init__(self,
            objectStatuses=NotImplemented,
            objectId=NotImplemented,
            orderBy=NotImplemented,
            searchOperator=NotImplemented):
        KalturaESearchParams.__init__(self,
            objectStatuses,
            objectId,
            orderBy)

        # @var KalturaESearchCategoryOperator
        self.searchOperator = searchOperator


    PROPERTY_LOADERS = {
        'searchOperator': (KalturaObjectFactory.create, 'KalturaESearchCategoryOperator'), 
    }

    def fromXml(self, node):
        KalturaESearchParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchParams.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryParams")
        kparams.addObjectIfDefined("searchOperator", self.searchOperator)
        return kparams

    def getSearchOperator(self):
        return self.searchOperator

    def setSearchOperator(self, newSearchOperator):
        self.searchOperator = newSearchOperator


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryResult(KalturaESearchResult):
    def __init__(self,
            highlight=NotImplemented,
            itemsData=NotImplemented,
            object=NotImplemented):
        KalturaESearchResult.__init__(self,
            highlight,
            itemsData)

        # @var KalturaCategory
        self.object = object


    PROPERTY_LOADERS = {
        'object': (KalturaObjectFactory.create, 'KalturaCategory'), 
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryResult")
        kparams.addObjectIfDefined("object", self.object)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject


# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            cuePointType=NotImplemented,
            id=NotImplemented,
            name=NotImplemented,
            text=NotImplemented,
            tags=NotImplemented,
            startTime=NotImplemented,
            endTime=NotImplemented,
            subType=NotImplemented,
            question=NotImplemented,
            answers=NotImplemented,
            hint=NotImplemented,
            explanation=NotImplemented,
            assetId=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.cuePointType = cuePointType

        # @var string
        self.id = id

        # @var string
        self.name = name

        # @var string
        self.text = text

        # @var array of KalturaString
        self.tags = tags

        # @var string
        self.startTime = startTime

        # @var string
        self.endTime = endTime

        # @var string
        self.subType = subType

        # @var string
        self.question = question

        # @var array of KalturaString
        self.answers = answers

        # @var string
        self.hint = hint

        # @var string
        self.explanation = explanation

        # @var string
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'cuePointType': getXmlNodeText, 
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'text': getXmlNodeText, 
        'tags': (KalturaObjectFactory.createArray, 'KalturaString'), 
        'startTime': getXmlNodeText, 
        'endTime': getXmlNodeText, 
        'subType': getXmlNodeText, 
        'question': getXmlNodeText, 
        'answers': (KalturaObjectFactory.createArray, 'KalturaString'), 
        'hint': getXmlNodeText, 
        'explanation': getXmlNodeText, 
        'assetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCuePointItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchCuePointItemData")
        kparams.addStringIfDefined("cuePointType", self.cuePointType)
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("text", self.text)
        kparams.addArrayIfDefined("tags", self.tags)
        kparams.addStringIfDefined("startTime", self.startTime)
        kparams.addStringIfDefined("endTime", self.endTime)
        kparams.addStringIfDefined("subType", self.subType)
        kparams.addStringIfDefined("question", self.question)
        kparams.addArrayIfDefined("answers", self.answers)
        kparams.addStringIfDefined("hint", self.hint)
        kparams.addStringIfDefined("explanation", self.explanation)
        kparams.addStringIfDefined("assetId", self.assetId)
        return kparams

    def getCuePointType(self):
        return self.cuePointType

    def setCuePointType(self, newCuePointType):
        self.cuePointType = newCuePointType

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getText(self):
        return self.text

    def setText(self, newText):
        self.text = newText

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getSubType(self):
        return self.subType

    def setSubType(self, newSubType):
        self.subType = newSubType

    def getQuestion(self):
        return self.question

    def setQuestion(self, newQuestion):
        self.question = newQuestion

    def getAnswers(self):
        return self.answers

    def setAnswers(self, newAnswers):
        self.answers = newAnswers

    def getHint(self):
        return self.hint

    def setHint(self, newHint):
        self.hint = newHint

    def getExplanation(self):
        return self.explanation

    def setExplanation(self, newExplanation):
        self.explanation = newExplanation

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchEntryOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchEntryOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryOperator(KalturaESearchEntryBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchEntryBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchEntryBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchEntryBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchEntryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryOperator")
        kparams.addIntEnumIfDefined("operator", self.operator)
        kparams.addArrayIfDefined("searchItems", self.searchItems)
        return kparams

    def getOperator(self):
        return self.operator

    def setOperator(self, newOperator):
        self.operator = newOperator

    def getSearchItems(self):
        return self.searchItems

    def setSearchItems(self, newSearchItems):
        self.searchItems = newSearchItems


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryParams(KalturaESearchParams):
    def __init__(self,
            objectStatuses=NotImplemented,
            objectId=NotImplemented,
            orderBy=NotImplemented,
            searchOperator=NotImplemented):
        KalturaESearchParams.__init__(self,
            objectStatuses,
            objectId,
            orderBy)

        # @var KalturaESearchEntryOperator
        self.searchOperator = searchOperator


    PROPERTY_LOADERS = {
        'searchOperator': (KalturaObjectFactory.create, 'KalturaESearchEntryOperator'), 
    }

    def fromXml(self, node):
        KalturaESearchParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchParams.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryParams")
        kparams.addObjectIfDefined("searchOperator", self.searchOperator)
        return kparams

    def getSearchOperator(self):
        return self.searchOperator

    def setSearchOperator(self, newSearchOperator):
        self.searchOperator = newSearchOperator


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryResult(KalturaESearchResult):
    def __init__(self,
            highlight=NotImplemented,
            itemsData=NotImplemented,
            object=NotImplemented):
        KalturaESearchResult.__init__(self,
            highlight,
            itemsData)

        # @var KalturaBaseEntry
        self.object = object


    PROPERTY_LOADERS = {
        'object': (KalturaObjectFactory.create, 'KalturaBaseEntry'), 
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryResult")
        kparams.addObjectIfDefined("object", self.object)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject


# @package Kaltura
# @subpackage Client
class KalturaESearchMetadataItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented,
            valueText=NotImplemented,
            valueInt=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId

        # @var string
        self.valueText = valueText

        # @var int
        self.valueInt = valueInt


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
        'valueText': getXmlNodeText, 
        'valueInt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchMetadataItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchMetadataItemData")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        kparams.addStringIfDefined("valueText", self.valueText)
        kparams.addIntIfDefined("valueInt", self.valueInt)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldId(self):
        return self.metadataFieldId

    def setMetadataFieldId(self, newMetadataFieldId):
        self.metadataFieldId = newMetadataFieldId

    def getValueText(self):
        return self.valueText

    def setValueText(self, newValueText):
        self.valueText = newValueText

    def getValueInt(self):
        return self.valueInt

    def setValueInt(self, newValueInt):
        self.valueInt = newValueInt


# @package Kaltura
# @subpackage Client
class KalturaESearchMetadataOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchMetadataOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchMetadataOrderByItem")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId


# @package Kaltura
# @subpackage Client
class KalturaESearchUserOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchUserOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchUserOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchUserOperator(KalturaESearchUserBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchUserBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchUserBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchUserBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchUserBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchUserBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserOperator")
        kparams.addIntEnumIfDefined("operator", self.operator)
        kparams.addArrayIfDefined("searchItems", self.searchItems)
        return kparams

    def getOperator(self):
        return self.operator

    def setOperator(self, newOperator):
        self.operator = newOperator

    def getSearchItems(self):
        return self.searchItems

    def setSearchItems(self, newSearchItems):
        self.searchItems = newSearchItems


# @package Kaltura
# @subpackage Client
class KalturaESearchUserParams(KalturaESearchParams):
    def __init__(self,
            objectStatuses=NotImplemented,
            objectId=NotImplemented,
            orderBy=NotImplemented,
            searchOperator=NotImplemented):
        KalturaESearchParams.__init__(self,
            objectStatuses,
            objectId,
            orderBy)

        # @var KalturaESearchUserOperator
        self.searchOperator = searchOperator


    PROPERTY_LOADERS = {
        'searchOperator': (KalturaObjectFactory.create, 'KalturaESearchUserOperator'), 
    }

    def fromXml(self, node):
        KalturaESearchParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchParams.toParams(self)
        kparams.put("objectType", "KalturaESearchUserParams")
        kparams.addObjectIfDefined("searchOperator", self.searchOperator)
        return kparams

    def getSearchOperator(self):
        return self.searchOperator

    def setSearchOperator(self, newSearchOperator):
        self.searchOperator = newSearchOperator


# @package Kaltura
# @subpackage Client
class KalturaESearchUserResult(KalturaESearchResult):
    def __init__(self,
            highlight=NotImplemented,
            itemsData=NotImplemented,
            object=NotImplemented):
        KalturaESearchResult.__init__(self,
            highlight,
            itemsData)

        # @var KalturaUser
        self.object = object


    PROPERTY_LOADERS = {
        'object': (KalturaObjectFactory.create, 'KalturaUser'), 
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchUserResult")
        kparams.addObjectIfDefined("object", self.object)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject


# @package Kaltura
# @subpackage Client
class KalturaESearchAbstractCategoryItem(KalturaESearchCategoryBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchCategoryBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range

        # @var bool
        self.addHighlight = addHighlight


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'addHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaESearchCategoryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchAbstractCategoryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchCategoryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchAbstractCategoryItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
        kparams.addBoolIfDefined("addHighlight", self.addHighlight)
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def setSearchTerm(self, newSearchTerm):
        self.searchTerm = newSearchTerm

    def getItemType(self):
        return self.itemType

    def setItemType(self, newItemType):
        self.itemType = newItemType

    def getRange(self):
        return self.range

    def setRange(self, newRange):
        self.range = newRange

    def getAddHighlight(self):
        return self.addHighlight

    def setAddHighlight(self, newAddHighlight):
        self.addHighlight = newAddHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchAbstractEntryItem(KalturaESearchEntryBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchEntryBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range

        # @var bool
        self.addHighlight = addHighlight


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'addHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaESearchEntryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchAbstractEntryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchAbstractEntryItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
        kparams.addBoolIfDefined("addHighlight", self.addHighlight)
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def setSearchTerm(self, newSearchTerm):
        self.searchTerm = newSearchTerm

    def getItemType(self):
        return self.itemType

    def setItemType(self, newItemType):
        self.itemType = newItemType

    def getRange(self):
        return self.range

    def setRange(self, newRange):
        self.range = newRange

    def getAddHighlight(self):
        return self.addHighlight

    def setAddHighlight(self, newAddHighlight):
        self.addHighlight = newAddHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchAbstractUserItem(KalturaESearchUserBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchUserBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range

        # @var bool
        self.addHighlight = addHighlight


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'addHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaESearchUserBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchAbstractUserItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchUserBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchAbstractUserItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
        kparams.addBoolIfDefined("addHighlight", self.addHighlight)
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def setSearchTerm(self, newSearchTerm):
        self.searchTerm = newSearchTerm

    def getItemType(self):
        return self.itemType

    def setItemType(self, newItemType):
        self.itemType = newItemType

    def getRange(self):
        return self.range

    def setRange(self, newRange):
        self.range = newRange

    def getAddHighlight(self):
        return self.addHighlight

    def setAddHighlight(self, newAddHighlight):
        self.addHighlight = newAddHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryQuery(KalturaESearchCategoryBaseItem):
    def __init__(self,
            eSearchQuery=NotImplemented):
        KalturaESearchCategoryBaseItem.__init__(self)

        # @var string
        self.eSearchQuery = eSearchQuery


    PROPERTY_LOADERS = {
        'eSearchQuery': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchCategoryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryQuery.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchCategoryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryQuery")
        kparams.addStringIfDefined("eSearchQuery", self.eSearchQuery)
        return kparams

    def getESearchQuery(self):
        return self.eSearchQuery

    def setESearchQuery(self, newESearchQuery):
        self.eSearchQuery = newESearchQuery


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryQuery(KalturaESearchEntryBaseItem):
    def __init__(self,
            eSearchQuery=NotImplemented):
        KalturaESearchEntryBaseItem.__init__(self)

        # @var string
        self.eSearchQuery = eSearchQuery


    PROPERTY_LOADERS = {
        'eSearchQuery': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchEntryBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryQuery.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryQuery")
        kparams.addStringIfDefined("eSearchQuery", self.eSearchQuery)
        return kparams

    def getESearchQuery(self):
        return self.eSearchQuery

    def setESearchQuery(self, newESearchQuery):
        self.eSearchQuery = newESearchQuery


# @package Kaltura
# @subpackage Client
class KalturaESearchUserQuery(KalturaESearchUserBaseItem):
    def __init__(self,
            eSearchQuery=NotImplemented):
        KalturaESearchUserBaseItem.__init__(self)

        # @var string
        self.eSearchQuery = eSearchQuery


    PROPERTY_LOADERS = {
        'eSearchQuery': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchUserBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserQuery.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchUserBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserQuery")
        kparams.addStringIfDefined("eSearchQuery", self.eSearchQuery)
        return kparams

    def getESearchQuery(self):
        return self.eSearchQuery

    def setESearchQuery(self, newESearchQuery):
        self.eSearchQuery = newESearchQuery


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryEntryItem(KalturaESearchAbstractEntryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented,
            categoryEntryStatus=NotImplemented):
        KalturaESearchAbstractEntryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchCategoryEntryFieldName
        self.fieldName = fieldName

        # @var KalturaCategoryEntryStatus
        self.categoryEntryStatus = categoryEntryStatus


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCategoryEntryFieldName"), 
        'categoryEntryStatus': (KalturaEnumsFactory.createInt, "KalturaCategoryEntryStatus"), 
    }

    def fromXml(self, node):
        KalturaESearchAbstractEntryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryEntryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractEntryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryEntryItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        kparams.addIntEnumIfDefined("categoryEntryStatus", self.categoryEntryStatus)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName

    def getCategoryEntryStatus(self):
        return self.categoryEntryStatus

    def setCategoryEntryStatus(self, newCategoryEntryStatus):
        self.categoryEntryStatus = newCategoryEntryStatus


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryItem(KalturaESearchAbstractCategoryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchAbstractCategoryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchCategoryFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCategoryFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchAbstractCategoryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractCategoryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryMetadataItem(KalturaESearchAbstractCategoryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented):
        KalturaESearchAbstractCategoryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchAbstractCategoryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryMetadataItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractCategoryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryMetadataItem")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldId(self):
        return self.metadataFieldId

    def setMetadataFieldId(self, newMetadataFieldId):
        self.metadataFieldId = newMetadataFieldId


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryUserItem(KalturaESearchAbstractCategoryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented,
            permissionLevel=NotImplemented,
            permissionName=NotImplemented):
        KalturaESearchAbstractCategoryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchCategoryUserFieldName
        self.fieldName = fieldName

        # @var KalturaCategoryUserPermissionLevel
        self.permissionLevel = permissionLevel

        # @var string
        self.permissionName = permissionName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCategoryUserFieldName"), 
        'permissionLevel': (KalturaEnumsFactory.createInt, "KalturaCategoryUserPermissionLevel"), 
        'permissionName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchAbstractCategoryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryUserItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractCategoryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryUserItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        kparams.addIntEnumIfDefined("permissionLevel", self.permissionLevel)
        kparams.addStringIfDefined("permissionName", self.permissionName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName

    def getPermissionLevel(self):
        return self.permissionLevel

    def setPermissionLevel(self, newPermissionLevel):
        self.permissionLevel = newPermissionLevel

    def getPermissionName(self):
        return self.permissionName

    def setPermissionName(self, newPermissionName):
        self.permissionName = newPermissionName


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryItem(KalturaESearchAbstractEntryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchAbstractEntryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchEntryFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchEntryFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchAbstractEntryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractEntryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchUnifiedItem(KalturaESearchAbstractEntryItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchAbstractEntryItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchAbstractEntryItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUnifiedItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractEntryItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUnifiedItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchUserItem(KalturaESearchAbstractUserItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchAbstractUserItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchUserFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchUserFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchAbstractUserItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractUserItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchUserMetadataItem(KalturaESearchAbstractUserItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented):
        KalturaESearchAbstractUserItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchAbstractUserItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserMetadataItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractUserItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserMetadataItem")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldId(self):
        return self.metadataFieldId

    def setMetadataFieldId(self, newMetadataFieldId):
        self.metadataFieldId = newMetadataFieldId


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryAbstractNestedItem(KalturaESearchEntryNestedBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchEntryNestedBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range

        # @var bool
        self.addHighlight = addHighlight


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'addHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaESearchEntryNestedBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryAbstractNestedItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryNestedBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryAbstractNestedItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
        kparams.addBoolIfDefined("addHighlight", self.addHighlight)
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def setSearchTerm(self, newSearchTerm):
        self.searchTerm = newSearchTerm

    def getItemType(self):
        return self.itemType

    def setItemType(self, newItemType):
        self.itemType = newItemType

    def getRange(self):
        return self.range

    def setRange(self, newRange):
        self.range = newRange

    def getAddHighlight(self):
        return self.addHighlight

    def setAddHighlight(self, newAddHighlight):
        self.addHighlight = newAddHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchNestedOperator(KalturaESearchEntryNestedBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchEntryNestedBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchEntryNestedBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchEntryNestedBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchEntryNestedBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchNestedOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryNestedBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchNestedOperator")
        kparams.addIntEnumIfDefined("operator", self.operator)
        kparams.addArrayIfDefined("searchItems", self.searchItems)
        return kparams

    def getOperator(self):
        return self.operator

    def setOperator(self, newOperator):
        self.operator = newOperator

    def getSearchItems(self):
        return self.searchItems

    def setSearchItems(self, newSearchItems):
        self.searchItems = newSearchItems


# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionItem(KalturaESearchEntryAbstractNestedItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchEntryAbstractNestedItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchCaptionFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCaptionFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchEntryAbstractNestedItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCaptionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryAbstractNestedItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCaptionItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointItem(KalturaESearchEntryAbstractNestedItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchEntryAbstractNestedItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchCuePointFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCuePointFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchEntryAbstractNestedItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCuePointItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryAbstractNestedItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCuePointItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryMetadataItem(KalturaESearchEntryAbstractNestedItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented):
        KalturaESearchEntryAbstractNestedItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchEntryAbstractNestedItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryMetadataItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchEntryAbstractNestedItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryMetadataItem")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldId(self):
        return self.metadataFieldId

    def setMetadataFieldId(self, newMetadataFieldId):
        self.metadataFieldId = newMetadataFieldId


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaESearchService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def searchCategory(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchCategory", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

    def searchEntry(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchEntry", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

    def searchUser(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchUser", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

########## main ##########
class KalturaElasticSearchClientPlugin(KalturaClientPlugin):
    # KalturaElasticSearchClientPlugin
    instance = None

    # @return KalturaElasticSearchClientPlugin
    @staticmethod
    def get():
        if KalturaElasticSearchClientPlugin.instance == None:
            KalturaElasticSearchClientPlugin.instance = KalturaElasticSearchClientPlugin()
        return KalturaElasticSearchClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'eSearch': KalturaESearchService,
        }

    def getEnums(self):
        return {
            'KalturaESearchItemType': KalturaESearchItemType,
            'KalturaESearchOperatorType': KalturaESearchOperatorType,
            'KalturaESearchCaptionFieldName': KalturaESearchCaptionFieldName,
            'KalturaESearchCategoryEntryFieldName': KalturaESearchCategoryEntryFieldName,
            'KalturaESearchCategoryFieldName': KalturaESearchCategoryFieldName,
            'KalturaESearchCategoryOrderByFieldName': KalturaESearchCategoryOrderByFieldName,
            'KalturaESearchCategoryUserFieldName': KalturaESearchCategoryUserFieldName,
            'KalturaESearchCuePointFieldName': KalturaESearchCuePointFieldName,
            'KalturaESearchEntryFieldName': KalturaESearchEntryFieldName,
            'KalturaESearchEntryOrderByFieldName': KalturaESearchEntryOrderByFieldName,
            'KalturaESearchSortOrder': KalturaESearchSortOrder,
            'KalturaESearchUserFieldName': KalturaESearchUserFieldName,
            'KalturaESearchUserOrderByFieldName': KalturaESearchUserOrderByFieldName,
        }

    def getTypes(self):
        return {
            'KalturaESearchBaseItem': KalturaESearchBaseItem,
            'KalturaESearchCategoryBaseItem': KalturaESearchCategoryBaseItem,
            'KalturaESearchEntryBaseItem': KalturaESearchEntryBaseItem,
            'KalturaESearchEntryBaseNestedObject': KalturaESearchEntryBaseNestedObject,
            'KalturaESearchEntryNestedBaseItem': KalturaESearchEntryNestedBaseItem,
            'KalturaESearchHighlight': KalturaESearchHighlight,
            'KalturaESearchItemData': KalturaESearchItemData,
            'KalturaESearchItemDataResult': KalturaESearchItemDataResult,
            'KalturaESearchOrderByItem': KalturaESearchOrderByItem,
            'KalturaESearchOrderBy': KalturaESearchOrderBy,
            'KalturaESearchParams': KalturaESearchParams,
            'KalturaESearchRange': KalturaESearchRange,
            'KalturaESearchResult': KalturaESearchResult,
            'KalturaESearchResponse': KalturaESearchResponse,
            'KalturaESearchUserBaseItem': KalturaESearchUserBaseItem,
            'KalturaESearchCaptionItemData': KalturaESearchCaptionItemData,
            'KalturaESearchCategoryOrderByItem': KalturaESearchCategoryOrderByItem,
            'KalturaESearchCategoryOperator': KalturaESearchCategoryOperator,
            'KalturaESearchCategoryParams': KalturaESearchCategoryParams,
            'KalturaESearchCategoryResult': KalturaESearchCategoryResult,
            'KalturaESearchCuePointItemData': KalturaESearchCuePointItemData,
            'KalturaESearchEntryOrderByItem': KalturaESearchEntryOrderByItem,
            'KalturaESearchEntryOperator': KalturaESearchEntryOperator,
            'KalturaESearchEntryParams': KalturaESearchEntryParams,
            'KalturaESearchEntryResult': KalturaESearchEntryResult,
            'KalturaESearchMetadataItemData': KalturaESearchMetadataItemData,
            'KalturaESearchMetadataOrderByItem': KalturaESearchMetadataOrderByItem,
            'KalturaESearchUserOrderByItem': KalturaESearchUserOrderByItem,
            'KalturaESearchUserOperator': KalturaESearchUserOperator,
            'KalturaESearchUserParams': KalturaESearchUserParams,
            'KalturaESearchUserResult': KalturaESearchUserResult,
            'KalturaESearchAbstractCategoryItem': KalturaESearchAbstractCategoryItem,
            'KalturaESearchAbstractEntryItem': KalturaESearchAbstractEntryItem,
            'KalturaESearchAbstractUserItem': KalturaESearchAbstractUserItem,
            'KalturaESearchCategoryQuery': KalturaESearchCategoryQuery,
            'KalturaESearchEntryQuery': KalturaESearchEntryQuery,
            'KalturaESearchUserQuery': KalturaESearchUserQuery,
            'KalturaESearchCategoryEntryItem': KalturaESearchCategoryEntryItem,
            'KalturaESearchCategoryItem': KalturaESearchCategoryItem,
            'KalturaESearchCategoryMetadataItem': KalturaESearchCategoryMetadataItem,
            'KalturaESearchCategoryUserItem': KalturaESearchCategoryUserItem,
            'KalturaESearchEntryItem': KalturaESearchEntryItem,
            'KalturaESearchUnifiedItem': KalturaESearchUnifiedItem,
            'KalturaESearchUserItem': KalturaESearchUserItem,
            'KalturaESearchUserMetadataItem': KalturaESearchUserMetadataItem,
            'KalturaESearchEntryAbstractNestedItem': KalturaESearchEntryAbstractNestedItem,
            'KalturaESearchNestedOperator': KalturaESearchNestedOperator,
            'KalturaESearchCaptionItem': KalturaESearchCaptionItem,
            'KalturaESearchCuePointItem': KalturaESearchCuePointItem,
            'KalturaESearchEntryMetadataItem': KalturaESearchEntryMetadataItem,
        }

    # @return string
    def getName(self):
        return 'elasticSearch'

