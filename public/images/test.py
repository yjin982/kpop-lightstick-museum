import os
import shutil

# 현재 스크립트 위치 기준 (이미지 폴더 경로로 수정하세요)
base_path = "./"  # 또는 실제 이미지 폴더 경로

rename_map = {
    # 루트
    "82Major(에투메).jpg": "82major.jpg",
    "pow(파우).jpg": "pow.jpg",
    
    # cjenm/
    "cjenm/웨이크원_이즈나.png": "cjenm/wakeone_izna.png",
    "cjenm/웨이크원_제로베이스원.jpg": "cjenm/wakeone_zerobaseone.jpg",
    "cjenm/웨이크원_케플러v1.png": "cjenm/wakeone_kep1er_v1.png",
    "cjenm/웨이크원_케플러v2.png": "cjenm/wakeone_kep1er_v2.png",
    
    # hybe/
    "hybe/미국레이블_캣츠아이.png": "hybe/uslabel_catseye.png",
    "hybe/빅히트_방탄소년단.jpg": "hybe/bighit_bts.jpg",
    "hybe/빅히트_투바투v1.webp": "hybe/bighit_txt_v1.webp",
    "hybe/빅히트_투바투v2.png": "hybe/bighit_txt_v2.png",
    "hybe/빌리프랩_아일릿.png": "hybe/beliftlab_illit.png",
    "hybe/빌리프랩_엔하이픈.png": "hybe/beliftlab_enhypen.png",
    "hybe/쏘스뮤직_르세라핌.png": "hybe/sourcemusic_lesserafim.png",
    "hybe/쏘스뮤직_여자친구v1.jpeg": "hybe/sourcemusic_gfriend_v1.jpeg",
    "hybe/쏘스뮤직_여자친구v2.jpg": "hybe/sourcemusic_gfriend_v2.jpg",
    "hybe/쏘스뮤직_여자친구v3.webp": "hybe/sourcemusic_gfriend_v3.webp",
    "hybe/어도어_뉴진스.png": "hybe/ador_newjeans.png",
    "hybe/일본레이블_앤팀.webp": "hybe/jpnlabel_andteam.webp",
    "hybe/케이오지_보이넥스트도어.webp": "hybe/kog_boynextdoor.webp",
    "hybe/플레디스_세븐틴v1.jpg": "hybe/pledis_seventeen_v1.jpg",
    "hybe/플레디스_세븐틴v2.jpg": "hybe/pledis_seventeen_v2.jpg",
    "hybe/플레디스_세븐틴v3.jpg": "hybe/pledis_seventeen_v3.jpg",
    "hybe/플레디스_투어스.png": "hybe/pledis_tws.png",
    
    # jyp/
    "jyp/데이식스.webp": "jyp/day6.webp",
    "jyp/스트레이키즈.jpg": "jyp/straykids.jpg",
    "jyp/엑디즈.webp": "jyp/xdinaryheroes.webp",
    "jyp/엔믹스.webp": "jyp/nmixx.webp",
    "jyp/있지.webp": "jyp/itzy.webp",
    "jyp/킥플립.webp": "jyp/kickflip.webp",
    "jyp/트와이스v1.png": "jyp/twice_v1.png",
    "jyp/트와이스v2.jpg": "jyp/twice_v2.jpg",
    
    # kakao/
    "kakao/스타쉽_몬스타엑스v1.jpg": "kakao/starship_monstax_v1.jpg",
    "kakao/스타쉽_몬스타엑스v2.webp": "kakao/starship_monstax_v2.webp",
    "kakao/스타쉽_아이브.webp": "kakao/starship_ive.webp",
    "kakao/스타쉽_아이브v2.webp": "kakao/starship_ive_v2.webp",
    "kakao/스타쉽_우주소녀.jpg": "kakao/starship_wjsn.jpg",
    "kakao/스타쉽_크래비티.jpg": "kakao/starship_cravity.jpg",
    "kakao/이담_아이유.jpg": "kakao/edam_iu.jpg",
    "kakao/하이업_스테이씨.jpg": "kakao/highup_stayc.jpg",
    
    # sm/
    "sm/동방신기.jpg": "sm/tvxq.jpg",
    "sm/라이즈.webp": "sm/riize.webp",
    "sm/레드벨벳.jpg": "sm/redvelvet.jpg",
    "sm/보아.jpg": "sm/boa.jpg",
    "sm/샤이니v3.jpg": "sm/shinee_v3.jpg",
    "sm/소녀시대.jpg": "sm/snsd.jpg",
    "sm/슈퍼주니어.jpg": "sm/superjunior.jpg",
    "sm/슈퍼주니어v2.jpg": "sm/superjunior_v2.jpg",
    "sm/에스파.webp": "sm/aespa.webp",
    "sm/에스파v2.jpg": "sm/aespa_v2.jpg",
    "sm/엑소v2.jpg": "sm/exo_v2.jpg",
    "sm/엔시티.png": "sm/nct.png",
    "sm/엔시티127.png": "sm/nct127.png",
    "sm/엔시티드림.png": "sm/nctdream.png",
    "sm/엔시티위시.png": "sm/nctwish.png",
    "sm/웨이션v1.jpg": "sm/wayv_v1.jpg",
    "sm/웨이션v2.png": "sm/wayv_v2.png",
    
    # yg/
    "yg/미야오.png": "yg/meovv.png",
    "yg/베이비몬스터.jpg": "yg/babymonster.jpg",
    "yg/블랙핑크.webp": "yg/blackpink.webp",
    "yg/위너v1.jpg": "yg/winner_v1.jpg",
    "yg/위너v2.webp": "yg/winner_v2.webp",
    "yg/지디.jpg": "yg/gdragon.jpg",
    "yg/트레저.jpg": "yg/.jpg",
    
    # 기타
    "더보이즈.webp": "theboyz.webp",
    "드림캐쳐.jpg": "dreamcatcher.jpg",
    "라잇썸.png": "lightsum.png",
    "루셈블.webp": "limelight.webp",
    "리베란테.jpg": "libelante.jpg",
    "리센느.jpg": "rescene.jpg",
    "마마무.webp": "mamamoo.webp",
    "모모랜드.png": "momoland.png",
    "배너.jpg": "vanner.jpg",
    "브레이브걸스.jpg": "bravegirls.jpg",
    "블락비.jpg": "blockb.jpg",
    "비비지.jpg": "viviz.jpg",
    "비투비.jpg": "btob.jpg",
    "빌리.jpg": "billlie.jpg",
    "아르테미스.webp": "artms.webp",
    "아이콘v1.jpeg": "ikon_v1.jpeg",
    "아이콘v2.jpg": "ikon_v2.jpg",
    "에이스.jpg": "ace.jpg",
    "엔플라잉.jpg": "nflying.jpg",
    "여자아이들.jpg": "gidle.jpg",
    "오마이걸.jpg": "ohmygirl.jpg",
    "온앤오프.webp": "onf.webp",
    "위아이.webp": "wei.webp",
    "위클리.jpg": "weeekly.jpg",
    "이달소.webp": "artms2.webp",
    "이달의소녀.jpeg": "loona.jpeg",
    "인피니트.png": "infinite.png",
    "키스오브라이프.jpg": "kissoflife.jpg",
    "트리플에스.webp": "triples.webp",
    "펜타곤.png": "pentagon.png",
    "프로미스나인.webp": "fromis9.webp",
    "플레이브.png": "plave.png",
    "하이라이트.webp": "highlight.webp",
    "하이키.jpg": "h1key.jpg",
}

def rename_files():
    os.chdir(base_path)
    
    success_count = 0
    error_count = 0
    
    for old_name, new_name in rename_map.items():
        try:
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                print(f"✅ {old_name} → {new_name}")
                success_count += 1
            else:
                print(f"⚠️  파일 없음: {old_name}")
                error_count += 1
        except Exception as e:
            print(f"❌ 오류 ({old_name}): {e}")
            error_count += 1
    
    print(f"\n완료! 성공: {success_count}, 실패/없음: {error_count}")

if __name__ == "__main__":
    print(f"작업 경로: {os.path.abspath(base_path)}")
    confirm = input("파일명을 변경하시겠습니까? (y/n): ")
    
    if confirm.lower() == 'y':
        rename_files()
    else:
        print("취소되었습니다.")