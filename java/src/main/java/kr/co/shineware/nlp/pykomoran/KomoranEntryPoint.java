package kr.co.shineware.nlp.pykomoran;

import kr.co.shineware.nlp.komoran.constant.DEFAULT_MODEL;
import kr.co.shineware.nlp.komoran.core.Komoran;
import kr.co.shineware.nlp.komoran.model.KomoranResult;
import kr.co.shineware.nlp.komoran.model.Token;
import kr.co.shineware.util.common.model.Pair;
import py4j.GatewayServer;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class KomoranEntryPoint {
    private Komoran komoran = null;
    private KomoranResult result = null;

    public void KomoranEntryPoint() {
    }

    public void init(String modelPath) {
        if (!new File(modelPath).exists()) {
            return;
        }

        try {
            komoran = new Komoran(modelPath);
        }
        // TODO: Modify Komoran throws FileNotFoundException
        catch (Exception e) {
            // FileNotFoundException => Invalid model path
        }
    }

    public boolean isInitialized() {
        if (komoran instanceof Komoran) {
            return true;
        }

        return false;
    }

    public void initByModel(DEFAULT_MODEL modelType) {
        komoran = new Komoran(modelType);
    }

    public void setUserDic(String userDicPath) {
        komoran.setUserDic(userDicPath);
    }

    public void setFWDic(String fwDicPath) {
        komoran.setFWDic(fwDicPath);
    }

    public void analyze(String sentence) {
        result = komoran.analyze(sentence);
    }

    public List<String> getNouns() {
        return result.getNouns();
    }

    public List<String> getMorphesByTags(List<String> targetPosCollection) {
        return result.getMorphesByTags(targetPosCollection);
    }

    public String getPlainText() {
        return result.getPlainText();
    }

    public List<Map<String, Object>> getTokenList() {
        // @formatter:off
        return result.getTokenList()
                     .stream()
                     .map(this::convertTokenToMap)
                     .collect(Collectors.toList());
        // @formatter:on
    }

    public List<Map<String, String>> getList() {
        // @formatter:off
        return result.getList()
                     .stream()
                     .map(this::convertPairToMap)
                     .collect(Collectors.toList());
        // @formatter:on
    }

    private Map<String, Object> convertTokenToMap(Token token) {
        return new HashMap<String, Object>() {{
            put("morph", token.getMorph());
            put("pos", token.getPos());
            put("beginIndex", token.getBeginIndex());
            put("endIndex", token.getEndIndex());
        }};
    }

    private Map<String, String> convertPairToMap(Pair pair) {
        return new HashMap<String, String>() {{
            put("first", pair.getFirst().toString());
            put("second", pair.getSecond().toString());
        }};
    }

    public static void main(String[] args) {
        // Sample code for testing
        KomoranEntryPoint komoranEntryPoint = new KomoranEntryPoint();
        komoranEntryPoint.initByModel(DEFAULT_MODEL.LIGHT);
        komoranEntryPoint.analyze("① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.");
        System.out.println(komoranEntryPoint.getTokenList());

//        // Codes below are for debugging
//        GatewayServer gatewayServer = new GatewayServer(new KomoranEntryPoint(), 25335);
//        gatewayServer.start();
    }
}
