# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:45:46+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, EmailStr, Field, RootModel, constr


class Type(Enum):
    primary = 'primary'
    secondary = 'secondary'
    home = 'home'
    office = 'office'
    shipping = 'shipping'
    billing = 'billing'
    other = 'other'


class BadRequestResponse(BaseModel):
    detail: Optional[Union[str, Dict[str, Any]]] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Bad Request'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Invalid Params'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#requestvalidationerror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[400]
    )
    type_name: Optional[str] = Field(
        None,
        description='The type of error returned',
        examples=['RequestValidationError'],
    )


class AccountType(Enum):
    bank_account = 'bank_account'
    credit_card = 'credit_card'
    other = 'other'


class Currency(Enum):
    UNKNOWN_CURRENCY = 'UNKNOWN_CURRENCY'
    AED = 'AED'
    AFN = 'AFN'
    ALL = 'ALL'
    AMD = 'AMD'
    ANG = 'ANG'
    AOA = 'AOA'
    ARS = 'ARS'
    AUD = 'AUD'
    AWG = 'AWG'
    AZN = 'AZN'
    BAM = 'BAM'
    BBD = 'BBD'
    BDT = 'BDT'
    BGN = 'BGN'
    BHD = 'BHD'
    BIF = 'BIF'
    BMD = 'BMD'
    BND = 'BND'
    BOB = 'BOB'
    BOV = 'BOV'
    BRL = 'BRL'
    BSD = 'BSD'
    BTN = 'BTN'
    BWP = 'BWP'
    BYR = 'BYR'
    BZD = 'BZD'
    CAD = 'CAD'
    CDF = 'CDF'
    CHE = 'CHE'
    CHF = 'CHF'
    CHW = 'CHW'
    CLF = 'CLF'
    CLP = 'CLP'
    CNY = 'CNY'
    COP = 'COP'
    COU = 'COU'
    CRC = 'CRC'
    CUC = 'CUC'
    CUP = 'CUP'
    CVE = 'CVE'
    CZK = 'CZK'
    DJF = 'DJF'
    DKK = 'DKK'
    DOP = 'DOP'
    DZD = 'DZD'
    EGP = 'EGP'
    ERN = 'ERN'
    ETB = 'ETB'
    EUR = 'EUR'
    FJD = 'FJD'
    FKP = 'FKP'
    GBP = 'GBP'
    GEL = 'GEL'
    GHS = 'GHS'
    GIP = 'GIP'
    GMD = 'GMD'
    GNF = 'GNF'
    GTQ = 'GTQ'
    GYD = 'GYD'
    HKD = 'HKD'
    HNL = 'HNL'
    HRK = 'HRK'
    HTG = 'HTG'
    HUF = 'HUF'
    IDR = 'IDR'
    ILS = 'ILS'
    INR = 'INR'
    IQD = 'IQD'
    IRR = 'IRR'
    ISK = 'ISK'
    JMD = 'JMD'
    JOD = 'JOD'
    JPY = 'JPY'
    KES = 'KES'
    KGS = 'KGS'
    KHR = 'KHR'
    KMF = 'KMF'
    KPW = 'KPW'
    KRW = 'KRW'
    KWD = 'KWD'
    KYD = 'KYD'
    KZT = 'KZT'
    LAK = 'LAK'
    LBP = 'LBP'
    LKR = 'LKR'
    LRD = 'LRD'
    LSL = 'LSL'
    LTL = 'LTL'
    LVL = 'LVL'
    LYD = 'LYD'
    MAD = 'MAD'
    MDL = 'MDL'
    MGA = 'MGA'
    MKD = 'MKD'
    MMK = 'MMK'
    MNT = 'MNT'
    MOP = 'MOP'
    MRO = 'MRO'
    MUR = 'MUR'
    MVR = 'MVR'
    MWK = 'MWK'
    MXN = 'MXN'
    MXV = 'MXV'
    MYR = 'MYR'
    MZN = 'MZN'
    NAD = 'NAD'
    NGN = 'NGN'
    NIO = 'NIO'
    NOK = 'NOK'
    NPR = 'NPR'
    NZD = 'NZD'
    OMR = 'OMR'
    PAB = 'PAB'
    PEN = 'PEN'
    PGK = 'PGK'
    PHP = 'PHP'
    PKR = 'PKR'
    PLN = 'PLN'
    PYG = 'PYG'
    QAR = 'QAR'
    RON = 'RON'
    RSD = 'RSD'
    RUB = 'RUB'
    RWF = 'RWF'
    SAR = 'SAR'
    SBD = 'SBD'
    SCR = 'SCR'
    SDG = 'SDG'
    SEK = 'SEK'
    SGD = 'SGD'
    SHP = 'SHP'
    SLL = 'SLL'
    SOS = 'SOS'
    SRD = 'SRD'
    SSP = 'SSP'
    STD = 'STD'
    SVC = 'SVC'
    SYP = 'SYP'
    SZL = 'SZL'
    THB = 'THB'
    TJS = 'TJS'
    TMT = 'TMT'
    TND = 'TND'
    TOP = 'TOP'
    TRC = 'TRC'
    TRY = 'TRY'
    TTD = 'TTD'
    TWD = 'TWD'
    TZS = 'TZS'
    UAH = 'UAH'
    UGX = 'UGX'
    USD = 'USD'
    USN = 'USN'
    USS = 'USS'
    UYI = 'UYI'
    UYU = 'UYU'
    UZS = 'UZS'
    VEF = 'VEF'
    VND = 'VND'
    VUV = 'VUV'
    WST = 'WST'
    XAF = 'XAF'
    XAG = 'XAG'
    XAU = 'XAU'
    XBA = 'XBA'
    XBB = 'XBB'
    XBC = 'XBC'
    XBD = 'XBD'
    XCD = 'XCD'
    XDR = 'XDR'
    XOF = 'XOF'
    XPD = 'XPD'
    XPF = 'XPF'
    XPT = 'XPT'
    XTS = 'XTS'
    XXX = 'XXX'
    YER = 'YER'
    ZAR = 'ZAR'
    ZMK = 'ZMK'
    ZMW = 'ZMW'
    BTC = 'BTC'
    ETH = 'ETH'


class CustomField(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    description: Optional[str] = Field(
        None,
        description='More information about the custom field',
        examples=['Employee Level'],
        title='Description',
    )
    id: str = Field(..., examples=['2389328923893298'], title='ID')
    name: Optional[str] = Field(
        None,
        description='Name of the custom field.',
        examples=['employee_level'],
        title='Name',
    )
    value: Optional[Union[str, float, bool, List[str]]] = None


class Type1(Enum):
    primary = 'primary'
    secondary = 'secondary'
    work = 'work'
    personal = 'personal'
    billing = 'billing'
    other = 'other'


class Email(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    email: EmailStr = Field(..., examples=['elon@musk.com'])
    id: Optional[str] = Field(None, examples=['123'])
    type: Optional[Type1] = Field(None, examples=['primary'])


class LeadEventType(Enum):
    field_ = '*'
    lead_lead_created = 'lead.lead.created'
    lead_lead_updated = 'lead.lead.updated'
    lead_lead_deleted = 'lead.lead.deleted'


class LeadWebhookEvent(BaseModel):
    entity_id: Optional[str] = Field(
        None,
        description="The service provider's ID of the entity that triggered this event",
        examples=['123456ASDF'],
    )
    entity_type: Optional[str] = Field(
        None,
        description='The type entity that triggered this event',
        examples=['Company'],
    )
    entity_url: Optional[str] = Field(
        None,
        description='The url to retrieve entity detail.',
        examples=['https://unify.apideck.com/crm/contacts/123456'],
    )
    event_id: Optional[str] = Field(
        None,
        description='Unique reference to this request event',
        examples=['9755c355-56c3-4a2f-a2da-86ff4411fccb'],
    )
    execution_attempt: Optional[float] = Field(
        None,
        description='The current count this request event has been attempted',
        examples=[2],
    )
    occurred_at: Optional[str] = Field(
        None,
        description='ISO Datetime for when the original event occurred',
        examples=['2021-10-01T03:14:55.419Z'],
    )
    service_id: Optional[str] = Field(
        None, description='Service provider identifier', examples=['close']
    )
    event_type: Optional[LeadEventType] = None


class LeadsFilter(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    email: Optional[str] = Field(
        None, description='E-mail of the lead to filter on', examples=['elon@tesla.com']
    )
    first_name: Optional[str] = Field(
        None, description='First name of the lead to filter on', examples=['Elon']
    )
    last_name: Optional[str] = Field(
        None, description='Last name of the lead to filter on', examples=['Musk']
    )
    name: Optional[str] = Field(
        None, description='Name of the lead to filter on', examples=['Elon Musk']
    )


class By(Enum):
    created_at = 'created_at'
    updated_at = 'updated_at'
    name = 'name'
    first_name = 'first_name'
    last_name = 'last_name'
    email = 'email'


class Links(BaseModel):
    current: Optional[str] = Field(
        None,
        description='Link to navigate to the current page through the API',
        examples=['https://unify.apideck.com/crm/companies'],
    )
    next: Optional[str] = Field(
        None,
        description='Link to navigate to the previous page through the API',
        examples=[
            'https://unify.apideck.com/crm/companies?cursor=em9oby1jcm06OnBhZ2U6OjM'
        ],
    )
    previous: Optional[str] = Field(
        None,
        description='Link to navigate to the previous page through the API',
        examples=[
            'https://unify.apideck.com/crm/companies?cursor=em9oby1jcm06OnBhZ2U6OjE%3D'
        ],
    )


class Cursors(BaseModel):
    current: Optional[str] = Field(
        None,
        description='Cursor to navigate to the current page of results through the API',
        examples=['em9oby1jcm06OnBhZ2U6OjI='],
    )
    next: Optional[str] = Field(
        None,
        description='Cursor to navigate to the next page of results through the API',
        examples=['em9oby1jcm06OnBhZ2U6OjM='],
    )
    previous: Optional[str] = Field(
        None,
        description='Cursor to navigate to the previous page of results through the API',
        examples=['em9oby1jcm06OnBhZ2U6OjE='],
    )


class Meta(BaseModel):
    cursors: Optional[Cursors] = Field(
        None,
        description='Cursors to navigate to previous or next pages through the API',
    )
    items_on_page: Optional[int] = Field(
        None,
        description='Number of items returned in the data property of the response',
        examples=[50],
    )


class NotFoundResponse(BaseModel):
    detail: Optional[Union[str, Dict[str, Any]]] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Not Found'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Unknown Widget'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#entitynotfounderror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[404]
    )
    type_name: Optional[str] = Field(
        None, description='The type of error returned', examples=['EntityNotFoundError']
    )


class NotImplementedResponse(BaseModel):
    detail: Optional[Union[str, Dict[str, Any]]] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Not Implemented'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Unmapped Attribute'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#mappingerror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[501]
    )
    type_name: Optional[str] = Field(
        None, description='The type of error returned', examples=['MappingError']
    )


class PaymentRequiredResponse(BaseModel):
    detail: Optional[str] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
        examples=['You have reached your limit of 2000'],
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Payment Required'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Request Limit Reached'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#requestlimiterror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[402]
    )
    type_name: Optional[str] = Field(
        None, description='The type of error returned', examples=['RequestLimitError']
    )


class Type2(Enum):
    primary = 'primary'
    secondary = 'secondary'
    home = 'home'
    work = 'work'
    office = 'office'
    mobile = 'mobile'
    assistant = 'assistant'
    fax = 'fax'
    direct_dial_in = 'direct-dial-in'
    personal = 'personal'
    other = 'other'


class PhoneNumber(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    area_code: Optional[str] = Field(None, examples=['323'], title='Area code')
    country_code: Optional[str] = Field(None, examples=['1'], title='Country code')
    extension: Optional[str] = Field(None, examples=['105'], title='Phone extension')
    id: Optional[str] = Field(None, examples=['12345'])
    number: constr(min_length=1) = Field(
        ..., examples=['111-111-1111'], title='Phone number'
    )
    type: Optional[Type2] = Field(None, examples=['primary'])


class RowVersion(RootModel[Optional[str]]):
    root: Optional[str] = Field(
        None,
        description='A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object.',
        examples=['1-12345'],
        title='Row version',
    )


class SocialLink(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[str] = Field(None, examples=['12345'])
    type: Optional[str] = Field(None, examples=['twitter'])
    url: constr(min_length=1) = Field(
        ..., examples=['https://www.twitter.com/apideck-io']
    )


class SortDirection(Enum):
    asc = 'asc'
    desc = 'desc'


class Tags(RootModel[List[str]]):
    root: List[str] = Field(..., examples=[['New']])


class Detail(BaseModel):
    context: Optional[str] = None
    error: Optional[Dict[str, Any]] = None


class TooManyRequestsResponse(BaseModel):
    detail: Optional[Detail] = None
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 6585)',
        examples=['Too Many Requests'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Connector Rate Limit Error'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#connectorratelimiterror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[429]
    )
    type_name: Optional[str] = Field(
        None,
        description='The type of error returned',
        examples=['ConnectorRateLimitError'],
    )


class UnauthorizedResponse(BaseModel):
    detail: Optional[str] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
        examples=[
            'Failed to generate valid JWT Session. Verify applicationId is correct'
        ],
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Unauthorized'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Unauthorized Request'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#unauthorizederror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[401]
    )
    type_name: Optional[str] = Field(
        None, description='The type of error returned', examples=['UnauthorizedError']
    )


class UnexpectedErrorResponse(BaseModel):
    detail: Optional[Union[str, Dict[str, Any]]] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Bad Request'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Invalid Params'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#unauthorizederror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[400]
    )
    type_name: Optional[str] = Field(
        None,
        description='The type of error returned',
        examples=['RequestHeadersValidationError'],
    )


class UnifiedId(BaseModel):
    id: str = Field(
        ...,
        description='The unique identifier of the resource',
        examples=['12345'],
        title='Id',
    )


class UnprocessableResponse(BaseModel):
    detail: Optional[str] = Field(
        None,
        description='Contains parameter or domain specific information related to the error and why it occurred.',
        examples=[
            'Unprocessable request, please verify your request headers and body.'
        ],
    )
    error: Optional[str] = Field(
        None,
        description='Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)',
        examples=['Unprocessable Entity'],
    )
    message: Optional[str] = Field(
        None,
        description='A human-readable message providing more details about the error.',
        examples=['Invalid State'],
    )
    ref: Optional[str] = Field(
        None,
        description='Link to documentation of error type',
        examples=['https://developers.apideck.com/errors#invalidstateerror'],
    )
    status_code: Optional[float] = Field(
        None, description='HTTP status code', examples=[422]
    )
    type_name: Optional[str] = Field(
        None, description='The type of error returned', examples=['InvalidStateError']
    )


class UpdateLeadResponse(BaseModel):
    data: UnifiedId
    operation: str = Field(..., description='Operation performed', examples=['update'])
    resource: str = Field(
        ..., description='Unified API resource name', examples=['companies']
    )
    service: str = Field(
        ..., description='Apideck ID of service provider', examples=['zoho-crm']
    )
    status: str = Field(..., description='HTTP Response Status', examples=['OK'])
    status_code: int = Field(
        ..., description='HTTP Response Status Code', examples=[200]
    )


class Type3(Enum):
    primary = 'primary'
    secondary = 'secondary'
    work = 'work'
    personal = 'personal'
    other = 'other'


class Website(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: Optional[str] = Field(None, examples=['12345'])
    type: Optional[Type3] = Field(None, examples=['primary'])
    url: constr(min_length=1) = Field(..., examples=['http://example.com'])


class Address(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    city: Optional[str] = Field(
        None, description='Name of city.', examples=['San Francisco']
    )
    contact_name: Optional[str] = Field(None, examples=['Elon Musk'])
    country: Optional[str] = Field(
        None,
        description='country code according to ISO 3166-1 alpha-2.',
        examples=['US'],
    )
    county: Optional[str] = Field(
        None,
        description='Address field that holds a sublocality, such as a county',
        examples=['Santa Clara'],
    )
    email: Optional[str] = Field(None, examples=['elon@musk.com'])
    fax: Optional[str] = Field(None, examples=['122-111-1111'])
    id: Optional[str] = Field(None, examples=['123'])
    latitude: Optional[str] = Field(None, examples=['40.759211'])
    line1: Optional[str] = Field(
        None,
        description='Line 1 of the address e.g. number, street, suite, apt #, etc.',
        examples=['Main street'],
    )
    line2: Optional[str] = Field(
        None, description='Line 2 of the address', examples=['apt #']
    )
    line3: Optional[str] = Field(
        None, description='Line 3 of the address', examples=['Suite #']
    )
    line4: Optional[str] = Field(
        None, description='Line 4 of the address', examples=['delivery instructions']
    )
    longitude: Optional[str] = Field(None, examples=['-73.984638'])
    name: Optional[str] = Field(None, examples=['HQ US'])
    phone_number: Optional[str] = Field(None, examples=['111-111-1111'])
    postal_code: Optional[str] = Field(
        None, description='Zip code or equivalent.', examples=['94104']
    )
    row_version: Optional[RowVersion] = None
    salutation: Optional[str] = Field(None, examples=['Mr'])
    state: Optional[str] = Field(None, description='Name of state', examples=['CA'])
    street_number: Optional[str] = Field(
        None, description='Street number', examples=['25']
    )
    string: Optional[str] = Field(
        None,
        examples=['25 Spring Street, Blackburn, VIC 3130'],
        title="The address string. Some APIs don't provide structured address data.",
    )
    type: Optional[Type] = Field(None, examples=['primary'])
    website: Optional[str] = Field(None, examples=['https://elonmusk.com'])


class BankAccount(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    account_name: Optional[str] = Field(
        None,
        description='The name which you used in opening your bank account.',
        examples=['SPACEX LLC'],
        title='Bank Account Name',
    )
    account_number: Optional[str] = Field(
        None,
        description='A bank account number is a number that is tied to your bank account. If you have several bank accounts, such as personal, joint, business (and so on), each account will have a different account number.',
        examples=['123465'],
        title='Bank Account Number',
    )
    account_type: Optional[AccountType] = Field(
        None,
        description='The type of bank account.',
        examples=['credit_card'],
        title='Account Type',
    )
    bank_code: Optional[str] = Field(
        None,
        description='A bank code is a code assigned by a central bank, a bank supervisory body or a Bankers Association in a country to all its licensed member banks or financial institutions.',
        examples=['BNH'],
        title='Bank Code',
    )
    bic: Optional[str] = Field(None, examples=['AUDSCHGGXXX'])
    branch_identifier: Optional[str] = Field(
        None,
        description='A branch identifier is a unique identifier for a branch of a bank or financial institution.',
        examples=['001'],
        title='Branch Identifier',
    )
    bsb_number: Optional[str] = Field(
        None,
        description='A BSB is a 6 digit numeric code used for identifying the branch of an Australian or New Zealand bank or financial institution.',
        examples=['062-001'],
        title='BSB Number',
    )
    currency: Optional[Currency] = None
    iban: Optional[str] = Field(None, examples=['CH2989144532982975332'])


class CreateLeadResponse(BaseModel):
    data: UnifiedId
    operation: str = Field(..., description='Operation performed', examples=['add'])
    resource: str = Field(
        ..., description='Unified API resource name', examples=['companies']
    )
    service: str = Field(
        ..., description='Apideck ID of service provider', examples=['zoho-crm']
    )
    status: str = Field(..., description='HTTP Response Status', examples=['OK'])
    status_code: int = Field(
        ..., description='HTTP Response Status Code', examples=[200]
    )


class DeleteLeadResponse(BaseModel):
    data: UnifiedId
    operation: str = Field(..., description='Operation performed', examples=['delete'])
    resource: str = Field(
        ..., description='Unified API resource name', examples=['companies']
    )
    service: str = Field(
        ..., description='Apideck ID of service provider', examples=['zoho-crm']
    )
    status: str = Field(..., description='HTTP Response Status', examples=['OK'])
    status_code: int = Field(
        ..., description='HTTP Response Status Code', examples=[200]
    )


class Lead(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    addresses: Optional[List[Address]] = None
    company_id: Optional[str] = Field(None, examples=['2'])
    company_name: str = Field(..., examples=['Spacex'])
    contact_id: Optional[str] = Field(None, examples=['2'])
    created_at: Optional[str] = Field(None, examples=['2020-09-30T07:43:32.000Z'])
    currency: Optional[Currency] = None
    custom_fields: Optional[List[CustomField]] = None
    description: Optional[str] = Field(None, examples=['A thinker'])
    emails: Optional[List[Email]] = None
    fax: Optional[str] = Field(None, examples=['+12129876543'])
    first_name: Optional[str] = Field(None, examples=['Elon'])
    id: Optional[str] = Field(None, examples=['12345'])
    language: Optional[str] = Field(
        None,
        description='language code according to ISO 639-1. For the United States - EN',
        examples=['EN'],
    )
    last_name: Optional[str] = Field(None, examples=['Musk'])
    lead_source: Optional[str] = Field(None, examples=['Cold Call'])
    monetary_amount: Optional[float] = Field(None, examples=[75000])
    name: constr(min_length=1) = Field(..., examples=['Elon Musk'])
    owner_id: Optional[str] = Field(None, examples=['54321'])
    phone_numbers: Optional[List[PhoneNumber]] = None
    prefix: Optional[str] = Field(None, examples=['Sir'])
    social_links: Optional[List[SocialLink]] = None
    status: Optional[str] = Field(None, examples=['New'])
    tags: Optional[Tags] = None
    title: Optional[str] = Field(None, examples=['CEO'])
    updated_at: Optional[str] = Field(None, examples=['2020-09-30T07:43:32.000Z'])
    websites: Optional[List[Website]] = None


class LeadsSort(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    by: Optional[By] = Field(
        None,
        description='The field on which to sort the Leads',
        examples=['created_at'],
    )
    direction: Optional[SortDirection] = 'asc'


class GetLeadResponse(BaseModel):
    data: Lead
    operation: str = Field(..., description='Operation performed', examples=['one'])
    resource: str = Field(
        ..., description='Unified API resource name', examples=['companies']
    )
    service: str = Field(
        ..., description='Apideck ID of service provider', examples=['zoho-crm']
    )
    status: str = Field(..., description='HTTP Response Status', examples=['OK'])
    status_code: int = Field(
        ..., description='HTTP Response Status Code', examples=[200]
    )


class GetLeadsResponse(BaseModel):
    data: List[Lead]
    links: Optional[Links] = None
    meta: Optional[Meta] = None
    operation: str = Field(..., description='Operation performed', examples=['all'])
    resource: str = Field(
        ..., description='Unified API resource name', examples=['companies']
    )
    service: str = Field(
        ..., description='Apideck ID of service provider', examples=['zoho-crm']
    )
    status: str = Field(..., description='HTTP Response Status', examples=['OK'])
    status_code: int = Field(
        ..., description='HTTP Response Status Code', examples=[200]
    )
