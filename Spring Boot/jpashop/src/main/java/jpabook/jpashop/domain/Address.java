package jpabook.jpashop.domain;

import jakarta.persistence.Embeddable;
import lombok.Getter;

@Embeddable @Getter
public class Address {

    private String city;
    private String street;
    private String zipcode;

    protected Address() {
    } // 함부로 기본생성자 사용 못하게 막아둠

    public Address(String city, String street, String zipcode){
        this.city = city;
        this.street = street;
        this.zipcode = zipcode;
    }


}
