# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 20:17
# @Author  : wwzhen
from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        name_dict = dict()
        for i in names:
            left = i.index('(')
            right = i.index(')')
            name_dict[i[0:left]] = i[left + 1:right]
        all_aynonyms = list()
        for i in synonyms:
            merge_flag = False
            place = i.index(',')
            item = i[0:1] + "'" + i[1:place] + "'" + i[place:place + 1] + "'" + i[place + 1: -1] + "'" + i[-1:]
            for j in range(len(all_aynonyms)):
                for k in eval(item):
                    if k in all_aynonyms[j]:
                        merge_flag = True
                        all_aynonyms[j] = all_aynonyms[j] + eval(item)
            else:
                if not merge_flag:
                    all_aynonyms.append(eval(item))
        result = list()
        for i in all_aynonyms:
            count = 0
            for j in list(set(i)):
                count = count + int(name_dict.get(j, 0))
                try:
                    del name_dict[j]
                except KeyError:
                    pass
            result.append(min(i) + "(" + str(count) + ")")
        for key in name_dict:
            result.append(key + "(" + str(name_dict[key]) + ")")
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.trulyMostPopular(
        ["Fcclu(70)", "Ommjh(63)", "Dnsay(60)", "Qbmk(45)", "Unsb(26)", "Gauuk(75)", "Wzyyim(34)", "Bnea(55)",
         "Kri(71)", "Qnaakk(76)", "Gnplfi(68)", "Hfp(97)", "Qoi(70)", "Ijveol(46)", "Iidh(64)", "Qiy(26)", "Mcnef(59)",
         "Hvueqc(91)", "Obcbxb(54)", "Dhe(79)", "Jfq(26)", "Uwjsu(41)", "Wfmspz(39)", "Ebov(96)", "Ofl(72)",
         "Uvkdpn(71)", "Avcp(41)", "Msyr(9)", "Pgfpma(95)", "Vbp(89)", "Koaak(53)", "Qyqifg(85)", "Dwayf(97)",
         "Oltadg(95)", "Mwwvj(70)", "Uxf(74)", "Qvjp(6)", "Grqrg(81)", "Naf(3)", "Xjjol(62)", "Ibink(32)", "Qxabri(41)",
         "Ucqh(51)", "Mtz(72)", "Aeax(82)", "Kxutz(5)", "Qweye(15)", "Ard(82)", "Chycnm(4)", "Hcvcgc(97)", "Knpuq(61)",
         "Yeekgc(11)", "Ntfr(70)", "Lucf(62)", "Uhsg(23)", "Csh(39)", "Txixz(87)", "Kgabb(80)", "Weusps(79)", "Nuq(61)",
         "Drzsnw(87)", "Xxmsn(98)", "Onnev(77)", "Owh(64)", "Fpaf(46)", "Hvia(6)", "Kufa(95)", "Chhmx(66)", "Avmzs(39)",
         "Okwuq(96)", "Hrschk(30)", "Ffwni(67)", "Wpagta(25)", "Npilye(14)", "Axwtno(57)", "Qxkjt(31)", "Dwifi(51)",
         "Kasgmw(95)", "Vgxj(11)", "Nsgbth(26)", "Nzaz(51)", "Owk(87)", "Yjc(94)", "Hljt(21)", "Jvqg(47)", "Alrksy(69)",
         "Tlv(95)", "Acohsf(86)", "Qejo(60)", "Gbclj(20)", "Nekuam(17)", "Meutux(64)", "Tuvzkd(85)", "Fvkhz(98)",
         "Rngl(12)", "Gbkq(77)", "Uzgx(65)", "Ghc(15)", "Qsc(48)", "Siv(47)"],
        ["(Gnplfi,Qxabri)", "(Uzgx,Siv)", "(Bnea,Lucf)", "(Qnaakk,Msyr)", "(Grqrg,Gbclj)", "(Uhsg,Qejo)",
         "(Csh,Wpagta)", "(Xjjol,Lucf)", "(Qoi,Obcbxb)", "(Npilye,Vgxj)", "(Aeax,Ghc)", "(Txixz,Ffwni)", "(Qweye,Qsc)",
         "(Kri,Tuvzkd)", "(Ommjh,Vbp)", "(Pgfpma,Xxmsn)", "(Uhsg,Csh)", "(Qvjp,Kxutz)", "(Qxkjt,Tlv)", "(Wfmspz,Owk)",
         "(Dwayf,Chycnm)", "(Iidh,Qvjp)", "(Dnsay,Rngl)", "(Qweye,Tlv)", "(Wzyyim,Kxutz)", "(Hvueqc,Qejo)", "(Tlv,Ghc)",
         "(Hvia,Fvkhz)", "(Msyr,Owk)", "(Hrschk,Hljt)", "(Owh,Gbclj)", "(Dwifi,Uzgx)", "(Iidh,Fpaf)", "(Iidh,Meutux)",
         "(Txixz,Ghc)", "(Gbclj,Qsc)", "(Kgabb,Tuvzkd)", "(Uwjsu,Grqrg)", "(Vbp,Dwayf)", "(Xxmsn,Chhmx)",
         "(Uxf,Uzgx)"]))

# ["Gauuk(75)", "Axwtno(57)", "Hfp(97)", "Jvqg(47)", "Fpaf(219)", "Aeax(646)", "Hljt(51)", "Gbkq(77)", "Chhmx(259)",
#  "Ebov(96)", "Chycnm(253)", "Acohsf(86)", "Dwifi(237)", "Kgabb(236)", "Obcbxb(124)", "Msyr(211)", "Dnsay(72)",
#  "Nuq(61)", "Ntfr(70)", "Ijveol(46)", "Csh(238)", "Yjc(94)", "Fcclu(70)", "Npilye(25)", "Bnea(179)", "Fvkhz(104)",
#  "Hcvcgc(97)", "Kufa(95)", "Gnplfi(109)", "Mwwvj(70)", "Mtz(72)", "Alrksy(69)", "Knpuq(61)", "Nsgbth(26)", "Yeekgc(11)",
#  "Uvkdpn(71)", "Nzaz(51)", "Avmzs(39)", "Kasgmw(95)", "Ofl(72)", "Oltadg(95)", "Unsb(26)", "Mcnef(59)", "Dhe(79)",
#  "Qyqifg(85)", "Onnev(77)", "Weusps(79)", "Koaak(53)", "Ucqh(51)", "Avcp(41)", "Qiy(26)", "Ard(82)", "Naf(3)",
#  "Jfq(26)", "Okwuq(96)", "Nekuam(17)", "Drzsnw(87)", "Qbmk(45)", "Ibink(32)"]
