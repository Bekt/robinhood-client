"""
Unofficial Robinhood API Python client.

Until the official documentation is out, all requests and responses
are simple JSON models. It does not make sense to be opiniated and
split endpoints into different resources and models right now.
"""


auth_token = None
api_base = 'https://api.robinhood.com'
api_version = '1.0'


def api_token_auth():
    """
    .. code-block:: none

      @POST("/api-token-auth/")
      AuthToken login(@Field("username") String paramString1,
          @Field("password") String paramString2)
    """
    raise NotImplementedError()


def api_token_logout():
    """
    .. code-block:: none

      @POST("/api-token-logout/")
      Response logOut()
    """
    raise NotImplementedError()


login = api_token_auth
logout = api_token_logout


class BaseResource(object):
    pass


class User(BaseResource):

    @classmethod
    def get(cls):
        """
        .. code-block:: none

           @GET("/user/")
           User getUser();
        """
        raise NotImplementedError()

    @classmethod
    def patch_user(cls):
        """
        .. code-block:: none

          @PATCH("/user/")
          User updateUser(@Body User.UpdateRequest paramUpdateRequest)
        """
        raise NotImplementedError()

    @classmethod
    def create(cls):
        """
        .. code-block:: none

          @PUT("/user/")
          User createUser(@Body User paramUser)
        """
        raise NotImplementedError()

    @classmethod
    def answer_cip_questions(cls):
        """
        .. code-block:: none

          @PUT("/user/cip_questions/")
          Response answerCipQuestions(@Body CipAnswerRequest paramCipAnswerRequest)
        """
        raise NotImplementedError()

    @classmethod
    def clip_questions(cls):
        """
        .. code-block:: none

          @GET("/user/cip_questions/")
          List<CipQuestion>> getCipQuestions()
        """
        raise NotImplementedError()

    @classmethod
    def identity_mismatch(cls):
        """
        .. code-block:: none

          @GET("/user/identity_mismatch/")
          PaginatedResult<IdentityMismatch> getMismatches()
        """
        raise NotImplementedError()

    @classmethod
    def additional_info(cls):
        """
        .. code-block:: none

          @GET("/user/additional_info/")
          UserAdditionalInfo getUserAdditionalInfo()
        """
        raise NotImplementedError()

    @classmethod
    def update_additional_info(cls):
        """
        .. code-block:: none

          @PUT("/user/additional_info/")
          UserAdditionalInfo submitUserAdditionalInfo(@Body UserAdditionalInfo paramUserAdditionalInfo)
        """
        raise NotImplementedError()

    @classmethod
    def basic_info(cls):
        """
        .. code-block:: none

          @GET("/user/basic_info/")
          UserBasicInfo getUserBasicInfo()
        """
        raise NotImplementedError()

    @classmethod
    def update_basic_info(cls):
        """
        .. code-block:: none

          @PUT("/user/basic_info/")
          UserBasicInfo submitUserBasicInfo(@Body UserBasicInfo paramUserBasicInfo)
        """
        raise NotImplementedError()

    @classmethod
    def patch_basic_info(self):
        """
        .. code-block:: none

          @PATCH("/user/basic_info/")
          UserBasicInfo updateUserBasicInfo(@Body UserBasicInfo paramUserBasicInfo)
        """
        raise NotImplementedError()

    @classmethod
    def employment(cls):
        """
        .. code-block:: none

          @GET("/user/employment/")
          UserEmployment getUserEmployment()
        """
        raise NotImplementedError()

    @classmethod
    def update_employment(cls):
        """
        .. code-block:: none

          @PUT("/user/employment/")
          UserEmployment submitUserEmployment(@Body UserEmployment paramUserEmployment)
        """
        raise NotImplementedError()

    @classmethod
    def investment_profile(cls):
        """
        .. code-block:: none

          @GET("/user/investment_profile/")
          UserInvestmentProfile getUserInvestmentProfile()
        """
        raise NotImplementedError()

    @classmethod
    def update_investment_profile(cls):
        """
        .. code-block:: none

          @PUT("/user/investment_profile/")
          Response submitUserInvestmentProfile(@Body UserInvestmentProfile paramUserInvestmentProfile)
        """
        raise NotImplementedError()


class Account(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/accounts/")
          PaginatedResult<Account> getAccounts()
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, account_id):
        """
        .. code-block:: none

          @GET("/accounts/{id}/")
          Account getAccount(@Path("id") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def recent_day_trades(cls, account_id):
        """
        .. code-block:: none

          @GET("/accounts/{id}/recent_day_trades/")
          PaginatedResult<DayTrade> getRecentDayTrades(@Path("id") String paramString)
        """
        raise NotImplementedError()


class Order(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/orders/")
          PaginatedResult<Order> getOrders(@Query("cursor") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, order_id):
        """
        .. code-block:: none

          @GET("/orders/{orderId}/")
          Order getOrder(@Path("orderId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def cancel(cls, order_id):
        """
        .. code-block:: none

          @POST("/orders/{orderId}/cancel/")
          Response cancelOrder(@Path("orderId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def post(cls):
        """
        .. code-block:: none

          @POST("/orders/")
          Order postOrder(@Body Order.Request paramRequest)
        """
        raise NotImplementedError()


class Notification(BaseResource):

    @classmethod
    def devices(cls):
        """
        .. code-block:: none

          @GET("/notifications/devices/")
          PaginatedResult<Device> getDevices()
        """
        raise NotImplementedError()

    @classmethod
    def get_device(cls, device_id):
        """
        .. code-block:: none

          @DELETE("/notifications/devices/{deviceId}/")
          Response deleteDevice(@Path("deviceId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def post_device(cls):
        """
        .. code-block:: none

          @POST("/notifications/devices/")
          Device postDevice(@Body Device paramDevice)
        """
        raise NotImplementedError()


class Application(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/applications/")
          PaginatedResult<Application> getApplications()
        """
        raise NotImplementedError()

    @classmethod
    def create(cls):
        """
        .. code-block:: none

          @PUT("/applications/individual/")
          Application createApplication()
        """
        raise NotImplementedError()

    @classmethod
    def get_by_type(cls, kind):
        """
        .. code-block:: none

          @GET("/applications/{type}/")
          Application getApplicationByType(@Path("type") String paramString)
        """
        raise NotImplementedError()


class Dividend(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/dividends/")
          PaginatedResult<Dividend> getDividends(@Query("cursor") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, dividend_id):
        """
        .. code-block:: none

          @GET("/dividends/{dividendId}/")
          Dividend getDividend(@Path("dividendId") String paramString)
        """
        raise NotImplementedError()


class Document(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/documents/")
          PaginatedResult<Document> getDocuments()
        """
        raise NotImplementedError()


    @classmethod
    def get(cls, document_id):
        """
        .. code-block:: none

          @GET("/documents/{id}/")
          Document getDocument(@Path("id") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def download(cls, document_id):
        """
        .. code-block:: none

          @GET("/documents/{id}/download/")
          Response getDocumentDownloadUrl(@Path("id") String paramString)
        """
        raise NotImplementedError()


class Ach(BaseResource):

    @classmethod
    def relationships(cls):
        """
        .. code-block:: none

          @GET("/ach/relationships/")
          PaginatedResult<AchRelationship> getAchRelationships(
              @Query("cursor") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def create_relationship(cls):
        """
        .. code-block:: none

          @POST("/ach/relationships/")
          AchRelationship createAchRelationship(@Field("account") String paramString1,
              @Field("bank_routing_number") String paramString2,
              @Field("bank_account_number") String paramString3,
              @Field("bank_account_type") String paramString4,
              @Field("bank_account_holder_name") String paramString5,
              @Field("bank_account_nickname") String paramString6)
        """
        raise NotImplementedError()

    @classmethod
    def get_relationship(cls, relationship_id):
        """
        .. code-block:: none

          @GET("/ach/relationships/{achRelationshipId}/")
          AchRelationship getAchRelationship(@Path("achRelationshipId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def unlink_relationship(cls, relationship_id):
        """
        .. code-block:: none

          @POST("/ach/relationships/{id}/unlink/")
          Response unlinkAchRelationship(@Path("id") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def verify_microdeposits(cls, relationship_id):
        """
        .. code-block:: none

          @POST("/ach/relationships/{id}/micro_deposits/verify/")
          Response verifyMicrodeposits(@Path("id") String paramString1,
              @Field("first_amount_cents") String paramString2,
              @Field("second_amount_cents") String paramString3)
        """
        raise NotImplementedError()

    @classmethod
    def get_transfer(cls, transfer_id):
        """
        .. code-block:: none

          @GET("/ach/transfers/{id}/")
          AchTransfer getAchTransfer(@Path("id") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def transfers(cls):
        """
        .. code-block:: none

          @GET("/ach/transfers/")
          PaginatedResult<AchTransfer> getAchTransfers(@Query("cursor") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def post_transfer(cls):
        """
        .. code-block:: none

          @POST("/ach/transfers/")
          AchTransfer postAchTransfer(@Body AchTransfer.Request paramRequest)
        """
        raise NotImplementedError()

    @classmethod
    def create_iav_relationship(cls):
        """
        .. code-block:: none

          @POST("/ach/iav/create/")
          AchRelationship createIavRelationship(@Field("access_token") String paramString1,
              @Field("iav_account_id") String paramString2,
              @Field("account") String paramString3,
              @Field("bank_account_type") String paramString4,
              @Field("bank_account_holder_name") String paramString5)
        """
        raise NotImplementedError()

    @classmethod
    def post_iav_mfa_answer(cls):
        """
        .. code-block:: none

          @POST("/ach/iav/auth/mfa/")
          IavResponse postIavAuthMfaAnswer(@Field("bank_institution") String paramString1,
              @Field("access_token") String paramString2,
              @Field("mfa") String paramString3)
        """
        raise NotImplementedError()

    @classmethod
    def post_iav_auth_request(cls):
        """
        .. code-block:: none

          @POST("/ach/iav/auth/")
          IavResponse postIavAuthRequest(@Field("bank_institution") String paramString1,
              @Field("username") String paramString2,
              @Field("password") String paramString3,
              @Field("pin") String paramString4)
        """
        raise NotImplementedError()

    @classmethod
    def queued_deposit(cls):
        """
        .. code-block:: none

          @GET("/ach/iav/queued_deposit/")
          QueuedAchDeposit getQueuedAchDeposit()
        """
        raise NotImplementedError()

    @classmethod
    def post_queued_deposit(cls):
        """
        .. code-block:: none

          @POST("/ach/iav/queued_deposit/")
          Response postQueuedAchDeposit(@Body QueuedAchDepositRequest paramQueuedAchDepositRequest)
        """
        raise NotImplementedError()

    @classmethod
    def automatic_deposits(cls):
        """
        .. code-block:: none

          @GET("/ach/deposit_schedules/")
          PaginatedResult<AutomaticDeposit> getAutomaticDeposits(@Query("cursor") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get_automatic_deposit(cls, deposit_id):
        """
        .. code-block:: none

          @GET("/ach/deposit_schedules/{automaticDepositId}/")
          AutomaticDeposit getAutomaticDeposit(@Path("automaticDepositId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def add_automatic_deposit(cls):
        """
        .. code-block:: none

          @POST("/ach/deposit_schedules/")
          AutomaticDeposit addAutomaticDeposit(@Body AutomaticDeposit.Request paramRequest)
        """
        raise NotImplementedError()

    @classmethod
    def delete_automatic_deposit(cls):
        """
        .. code-block:: none

          @DELETE("/ach/deposit_schedules/{automaticDepositId}/")
          Response deleteAutomaticDeposit(@Path("automaticDepositId") String paramString)
        """
        raise NotImplementedError()


class Watchlist(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/watchlists/")
          PaginatedResult<Watchlist> getWatchlists()
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, watchlist):
        """
        .. code-block:: none

          @GET("/watchlists/{watchlistName}/")
          PaginatedResult<WatchlistInstrument> getWatchlist(
              @Path("watchlistName") String paramString1,
              @Query("cursor") String paramString2)
        """
        raise NotImplementedError()

    @classmethod
    def create(cls):
        """
        .. code-block:: none

          @POST("/watchlists/")
          Watchlist.EmptyWatchlist createWatchlist(@Field("name") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def add_instrument(cls, watchlist, instrument):
        """
        .. code-block:: none

          @POST("/watchlists/{watchlistName}/")
          WatchlistInstrument addInstrument(@Path("watchlistName") String paramString1,
              @Field("instrument") String paramString2)
        """
        raise NotImplementedError()

    @classmethod
    def delete_instrument(cls, watchlist, instrument_id):
        """
        .. code-block:: none

          @DELETE("/watchlists/{watchlistName}/{instrumentId}/")
          Void deleteInstrument(@Path("watchlistName") String paramString1,
              @Path("instrumentId") String paramString2)
        """
        raise NotImplementedError()

    @classmethod
    def populate(cls):
        """
        .. code-block:: none

          @POST("/watchlists/{watchlist}/bulk_add/")
          List<WatchlistInstrument> populateWatchlist(@Path("watchlist") String paramString1,
              @Field("symbols") String paramString2)
        """
        raise NotImplementedError()


class Quote(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/quotes/")
          PaginatedResult<Quote getQuotes(@Query("symbols") String paramString1,
              @Query("cursor") String paramString2)
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, symbol):
        """
        .. code-block:: none

          @GET("/quotes/{symbol}/")
          Quote getQuote(@Path("symbol") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get_historical(cls, symbol):
        """
        .. code-block:: none

          @GET("/quotes/historicals/{symbol}/")
          HistoricalQuoteResult getHistoricalQuotes(@Path("symbol") String paramString1,
              @Query("interval") String paramString2)
        """
        raise NotImplementedError()


class Market(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/markets/")
          PaginatedResult<Market> getMarkets()
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, mic):
        """
        .. code-block:: none

          @GET("/markets/{mic}/")
          Market getMarket(@Path("mic") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def xnys_market_hours(cls, date):
        """
        .. code-block:: none

          @GET("/markets/XNYS/hours/{date}/")
          MarketHours getMarketHours(@Path("date") String paramString)
        """
        raise NotImplementedError()


class Upload(BaseResource):

    @classmethod
    def document_requests(cls):
        """
        .. code-block:: none

          @GET("/upload/document_requests/")
          PaginatedResult<DocumentRequest> getDocumentRequests()
        """
        raise NotImplementedError()

    @classmethod
    def get_document_request(cls, document_id):
        """
        .. code-block:: none

          @GET("/upload/document_requests/{id}/")
          DocumentRequest getDocumentRequest(@Path("id") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def mark_document_request_uploaded(cls, rhid):
        """
        .. code-block:: none

          @PATCH("/upload/document_requests/{rhid}/")
          DocumentRequest markDocumentRequestUploaded(@Path("rhid") String paramString1,
              @Field("state") String paramString2)
        """
        raise NotImplementedError()


class Midland(BaseResource):

    @classmethod
    def dismiss_card(cls, card_id):
        """
        .. code-block:: none

          @POST("/midlands/notifications/stack/{cardId}/dismiss/")
          Response dismissCard(@Path("cardId") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def card_stack(cls):
        """
        .. code-block:: none

          @GET("/midlands/notifications/stack/")
          Card.Stack getCardStack()
        """
        raise NotImplementedError()

    @classmethod
    def news(cls, symbol):
        """
        .. code-block:: none

          @GET("/midlands/news/{instrumentSymbol}/")
          PaginatedResult<News> getNews(@Path("instrumentSymbol") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def top_mover(cls, direction):
        """
        .. code-block:: none

          @GET("/midlands/movers/sp500/")
          PaginatedResult<TopMover> getTopMover(@Query("direction") String paramString)
        """
        raise NotImplementedError()


class Portfolio(BaseResource):

    @classmethod
    def get(cls, account_id):
        """
        .. code-block:: none

          @GET("/portfolios/{accountNumber}/")
          Portfolio getPortfolio(@Path("accountNumber") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get_historicals(cls, account_id):
        """
        .. code-block:: none

          @GET("/portfolios/historicals/{accountNumber}/")
          HistoricalPortfolio getHistoricalPortfolios(@Path("accountNumber") String paramString1,
              @Query("interval") String paramString2)
        """
        raise NotImplementedError()


class Position(BaseResource):

    @classmethod
    def get(cls, account_id, instrument):
        """
        .. code-block:: none

          @GET("/positions/{accountNumber}/{instrumentId}/")
          Position getPosition(@Path("accountNumber") String paramString1,
              @Path("instrumentId") String paramString2)
        """
        raise NotImplementedError()

    @classmethod
    def all(cls, account):
        """
        .. code-block:: none

          @GET("/positions/?nonzero=true")
          PaginatedResult<Position> getPositions(@Query("account") String paramString1,
              @Query("cursor") String paramString2)
        """
        raise NotImplementedError()


class Instrument(BaseResource):

    @classmethod
    def all(cls):
        """
        .. code-block:: none

          @GET("/instruments/")
          PaginatedResult<Instrument> queryInstruments(@Query("query") String paramString)
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, instrument_id):
        """
        .. code-block:: none

          @GET("/instruments/{instrumentId}/")
          Instrument getInstrument(@Path("instrumentId") String paramString)
        """
        raise NotImplementedError()
