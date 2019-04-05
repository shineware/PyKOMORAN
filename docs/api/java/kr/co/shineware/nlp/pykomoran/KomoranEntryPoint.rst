.. java:import:: kr.co.shineware.nlp.komoran.constant DEFAULT_MODEL

.. java:import:: kr.co.shineware.nlp.komoran.core Komoran

.. java:import:: kr.co.shineware.nlp.komoran.model KomoranResult

.. java:import:: kr.co.shineware.nlp.komoran.model Token

.. java:import:: kr.co.shineware.util.common.model Pair

.. java:import:: py4j GatewayServer

.. java:import:: java.io File

.. java:import:: java.io FileNotFoundException

.. java:import:: java.util.stream Collectors

KomoranEntryPoint
=================

.. java:package:: kr.co.shineware.nlp.pykomoran
   :noindex:

.. java:type:: public class KomoranEntryPoint

   KOMORAN을 Wrapping하는 Class로, Py4J에 의해 불리는 Java-side의 EntryPoint입니다. 직접 실행 시 main 메소드에서 Py4J의 GatewayServer를 띄웁니다. 사용법:

   .. parsed-literal::

      KomoranEntryPoint kep = new KomoranEntryPoint();
      kep.init(MODEL_PATH);

   :author: \ `9bow <https://github.com/9bow>`_\

   **See also:** :java:ref:`kr.co.shineware.nlp.komoran.core.Komoran`, :java:ref:`py4j.GatewayServer`

Methods
-------
KomoranEntryPoint
^^^^^^^^^^^^^^^^^

.. java:method:: public void KomoranEntryPoint()
   :outertype: KomoranEntryPoint

analyze
^^^^^^^

.. java:method:: public void analyze(String sentence)
   :outertype: KomoranEntryPoint

   내부 Komoran 객체에 주어진 sentence를 분석하여 내부 KomoranResult 객체에 저장합니다.

   :param sentence: 분석할 문장

getList
^^^^^^^

.. java:method:: public List<Map<String, String>> getList()
   :outertype: KomoranEntryPoint

   내부 KomoranResult 객체로부터 분석 결과를 Pair 형태로 반환받습니다. Python에서 이용할 수 있도록 Token 객체는 Map 객체로 변환하여 제공합니다.

   :return: 형태소 분석 결과의 Map(Pair) List

   **See also:** :java:ref:`kr.co.shineware.util.common.model.Pair`

getMorphesByTags
^^^^^^^^^^^^^^^^

.. java:method:: public List<String> getMorphesByTags(List<String> targetPosCollection)
   :outertype: KomoranEntryPoint

   내부 KomoranResult 객체로부터 주어진 품사의 형태소들만 반환받습니다.

   :param targetPosCollection: 품사 List
   :return: 주어진 형태소들에 해당하는 형태소 List

getNouns
^^^^^^^^

.. java:method:: public List<String> getNouns()
   :outertype: KomoranEntryPoint

   내부 KomoranResult 객체로부터 명사류의 형태소만 반환받습니다.

   :return: 분석 결과 중, 명사류의 형태소 List

getPlainText
^^^^^^^^^^^^

.. java:method:: public String getPlainText()
   :outertype: KomoranEntryPoint

   내부 KomoranResult 객체로부터 PlainText 형태의 분석 결과를 반환받습니다.

   :return: 전체 형태소 분석 결과의 PlainText

getTokenList
^^^^^^^^^^^^

.. java:method:: public List<Map<String, Object>> getTokenList()
   :outertype: KomoranEntryPoint

   내부 KomoranResult 객체로부터 분석 결과를 Token 형태로 반환받습니다. Python에서 이용할 수 있도록 Token 객체는 Map 객체로 변환하여 제공합니다.

   :return: 형태소 분석 결과의 Map(Token) List

   **See also:** :java:ref:`kr.co.shineware.nlp.komoran.model.Token`

init
^^^^

.. java:method:: public void init(String modelPath)
   :outertype: KomoranEntryPoint

   내부 Komoran 객체를 modelPath로 초기화합니다.

   :param modelPath: 모델이 위치한 절대 경로
   :throws FileNotFoundException: modelPath에 모델이 존재하지 않을 시 Exception 발생

   **See also:** :java:ref:`kr.co.shineware.nlp.komoran.model.Token`

initByModel
^^^^^^^^^^^

.. java:method:: public void initByModel(DEFAULT_MODEL modelType)
   :outertype: KomoranEntryPoint

   내부 Komoran 객체를 기본 modelType으로 초기화합니다. modelType은 KOMORAN의 DEFAULT_MODEL 타입입니다.

   :param modelType: DEFAULT_MODEL 종류

isInitialized
^^^^^^^^^^^^^

.. java:method:: public boolean isInitialized()
   :outertype: KomoranEntryPoint

   내부 Komoran 객체가 초기화되었는지 확인합니다.

   :return: 초기화 여부 (boolean)

main
^^^^

.. java:method:: public static void main(String[] args)
   :outertype: KomoranEntryPoint

   직접 실행 시 Py4J의 GatewayServer를 실행합니다.

   :param args:

   **See also:** :java:ref:`py4j.GatewayServer`

setFWDic
^^^^^^^^

.. java:method:: public void setFWDic(String fwDicPath)
   :outertype: KomoranEntryPoint

   내부 Komoran 객체에 기분석 사전을 적용합니다.

   :param fwDicPath: 기분석 사전이 위치한 절대 경로

setUserDic
^^^^^^^^^^

.. java:method:: public void setUserDic(String userDicPath)
   :outertype: KomoranEntryPoint

   내부 Komoran 객체에 사용자 사전을 적용합니다.

   :param userDicPath: 사용자 사전이 위치한 절대 경로

