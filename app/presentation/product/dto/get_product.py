from pydantic import BaseModel, ConfigDict


class GetProducts(BaseModel):
    # class Response(BaseModel):
    # id: int = Field(examples=[1])
    # name: str = Field(examples=["pencil"])
    # '''
    #     Field에서 정의를 내리고 싶으면 위처럼,
    # '''
    class Response(BaseModel):
        id: int
        name: str

        model_config = ConfigDict(
            # JSON 스키마 관련
            title="Product Response",  # 스키마 제목
            # 예시 정의
            json_schema_extra={"examples": [{"id": 1, "name": "pencil"}]},
            # 필드명 변환 (snake_case <-> camelCase)
            alias_generator=None,  # 또는 'to_camel', 'to_snake'
            # JSON 직렬화 시 별칭 사용 여부
            populate_by_name=True,  # 원래 필드명과 alias 둘 다 허용
            # 추가 필드 허용 여부
            extra="forbid",  # 'allow', 'ignore', 'forbid'
            # 검증 모드
            validate_assignment=True,  # 할당 시에도 검증
            validate_default=True,  # 기본값도 검증
            # # 문자열 처리
            str_strip_whitespace=True,  # 문자열 앞뒤 공백 제거
            str_to_lower=False,  # 문자열을 소문자로 변환
            str_to_upper=False,  # 문자열을 대문자로 변환
            # 기타 유용한 옵션들
            frozen=False,  # 불변 객체로 만들기
            # use_enum_values=True,       # Enum의 값 사용
            # arbitrary_types_allowed=False,  # 임의 타입 허용
        )
